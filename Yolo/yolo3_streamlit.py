import cv2
import numpy as np
import time
import streamlit as st
import tempfile

confThreshold = 0.5  # Default confidence threshold
nmsThreshold = 0.4   # Default non-maximum suppression threshold
inpWidth = 416       # Width of network's input image (must be consistent with the model)
inpHeight = 416      # Height of network's input image (must be consistent with the model)

# Load names of classes
classesFile = "YOLOWeight/coco.names"
classes = None
with open(classesFile, 'rt') as f:
    classes = f.read().rstrip('\n').split('\n')

# Give the configuration and weight files for the model and load the network.
modelConfiguration = "YOLOWeight/yolov3-tiny.cfg"
modelWeights = "YOLOWeight/yolov3-tiny.weights"

net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

# Get the names of the output layers
def getOutputsNames(net):
    layersNames = net.getLayerNames()
    return [layersNames[i-1] for i in net.getUnconnectedOutLayers()]

# Draw the predicted bounding box
def drawPred(classId, conf, left, top, right, bottom, frame):
    cv2.rectangle(frame, (left, top), (right, bottom), (255, 178, 50), 3)
    label = '%.2f' % conf
    if classes:
        assert(classId < len(classes))
        label = '%s:%s' % (classes[classId], label)

    labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    top = max(top, labelSize[1])
    cv2.rectangle(frame, (left, top - round(1.5*labelSize[1])), (left + round(1.5*labelSize[0]), top + baseLine), (255, 255, 255), cv2.FILLED)
    cv2.putText(frame, label, (left, top), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,0), 1)

# Remove the bounding boxes with low confidence using non-maxima suppression
def postprocess(frame, outs, confThreshold, nmsThreshold):
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]
    classIds = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                center_x = int(detection[0] * frameWidth)
                center_y = int(detection[1] * frameHeight)
                width = int(detection[2] * frameWidth)
                height = int(detection[3] * frameHeight)
                left = int(center_x - width / 2)
                top = int(center_y - height / 2)
                classIds.append(classId)
                confidences.append(float(confidence))
                boxes.append([left, top, width, height])

    indices = cv2.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)
    for i in indices:
        box = boxes[i]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3]
        drawPred(classIds[i], confidences[i], left, top, left + width, top + height, frame)

def main():
    st.title("YOLOv3-tiny Object Detection")
    st.write("Perform real-time object detection on a video stream, an uploaded file, or your webcam.")

    st.sidebar.header("Configuration")
    conf_threshold = st.sidebar.slider("Confidence Threshold", 0.0, 1.0, 0.5, 0.05)
    nms_threshold = st.sidebar.slider("NMS Threshold", 0.0, 1.0, 0.4, 0.05)

    source_option = st.sidebar.radio(
        "Select Input Source", ("Webcam", "Video File Upload", "Live Stream URL")
    )

    cap = None
    if source_option == "Webcam":
        st.info("Webcam selected. Make sure your webcam is enabled and press 'Run'.")
        # The number is the device index. 0 is usually the default webcam.
        cap = cv2.VideoCapture(0)
    elif source_option == "Video File Upload":
        uploaded_file = st.sidebar.file_uploader(
            "Upload a video file", type=["mp4", "avi", "mov", "mkv"]
        )
        if uploaded_file is not None:
            # Use a temporary file to stream the uploaded video
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(uploaded_file.read())
            cap = cv2.VideoCapture(tfile.name)
    elif source_option == "Live Stream URL":
        # Example public live stream: http://pendelcam.kip.uni-heidelberg.de/mjpg/video.mjpg
        video_url = st.text_input("Enter live stream URL", "rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov")
        if video_url:
            cap = cv2.VideoCapture(video_url)

    run = st.checkbox('Run')
    frame_placeholder = st.empty()

    if run and cap is not None:
        if not cap.isOpened():
            st.error(f"Error: Could not open video stream from '{source_option}'. Please check the source and permissions.")
        else:
            while run and cap.isOpened():
                stime = time.time()
                hasFrame, frame = cap.read()
                if not hasFrame:
                    st.write("The video stream has ended or the source is unavailable.")
                    break

                blob = cv2.dnn.blobFromImage(frame, 1/255, (inpWidth, inpHeight), [0,0,0], 1, crop=False)
                net.setInput(blob)
                outs = net.forward(getOutputsNames(net))
                postprocess(frame, outs, conf_threshold, nms_threshold)

                etime = time.time()
                # Avoid division by zero
                if etime > stime:
                    fps = 1 / (etime - stime)
                    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                frame_placeholder.image(frame, channels="BGR")

            cap.release()
    elif run and cap is None:
        st.warning("Please provide a valid URL to start the stream.")

if __name__ == '__main__':
    main()    # Add a section for YouTube live stream