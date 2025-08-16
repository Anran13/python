import cv2
import numpy as np
import time

confThreshold = 0.5  #Confidence threshold
nmsThreshold = 0.4   #Non-maximum suppression threshold
inpWidth = 640       #Width of network's input image
inpHeight = 480      #Height of network's input image

target = "image/face.jpg"
cap = cv2.VideoCapture(target)
modelConfiguration = "YOLOWeight/yolov4.cfg"
modelWeights = "YOLOWeight/yolov4.weights"

# Load names of classes
classesFile = "YOLOWeight/coco.names" 
#classesFile = "YOLOWeight-1/obj.names"
classes = None
with open(classesFile, 'rt') as f:
    classes = f.read().rstrip('\n').split('\n')

net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

# get connection
def getOutputsNames(net):
    layersNames = net.getLayerNames()
    return [layersNames[i-1] for i in net.getUnconnectedOutLayers()]

# label objects in rectangle frames
def drawPred(classId, conf, left, top, right, bottom, frame):
    cv2.rectangle(frame, (left, top), (right, bottom), (255, 178, 50), 3)
    label = '%.2f' % conf    
    # Get the label for the class name and its confidence
    if classes:
        assert(classId < len(classes))
        label = '%s:%s' % (classes[classId], label)

    #Display the label at the top of the bounding box
    labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    top = max(top, labelSize[1])
    cv2.rectangle(frame, (left, top - round(1.5*labelSize[1])), (left + round(1.5*labelSize[0]), top + baseLine), (255, 255, 255), cv2.FILLED)
    cv2.putText(frame, label, (left, top), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,0), 1)

# start analyzing
def postprocess(frame, outs):
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]
    classIds = []
    confidences = []
    boxes = []
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
        i = i
        box = boxes[i]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3]
        drawPred(classIds[i], confidences[i], left, top, left + width, top + height, frame)
        if classIds[i]==67:
            pass #cv2.imwrite("test.jpg", frame)
       

# Process inputs
while True:
    try:
        stime=time.time()
        hasFrame, frame = cap.read()
        blob = cv2.dnn.blobFromImage(frame, 1/255, (inpWidth, inpHeight), [0,0,0], 1, crop=False)

        net.setInput(blob)
        outs = net.forward(getOutputsNames(net))

        postprocess(frame, outs)

        etime = time.time()
        label = "fps=" + str(round(1/(etime-stime),2))
        cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),2)
        frame=cv2.resize(frame,(640,480))
        cv2.imshow("YOLO", frame)
    except Exception as e:
        print(e) 
        time.sleep(0.5)
        cap = cv2.VideoCapture(target)
    key=cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
