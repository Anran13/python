#請先安裝1.paho-mqtt、2.opencv
#pip3 install paho-mqtt
#pip install –v opencv–python

#再安裝1.MediaPipe 及 2.msvc-runtime
#pip install mediapipe
#pip install msvc-runtime

import mediapipe as mp
import cv2,time
import paho.mqtt.client as mqtt

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh
drawing_spec = mp_drawing.DrawingSpec(color=(0, 255, 0),thickness=1, circle_radius=1)
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True
                                  , min_detection_confidence=0.5, min_tracking_confidence=0.5)


MqttBroker="mqttgo.io"
MqttPort=1883
SubTopic1="test/myvideo"
 
#設定連線成功時的Callback
def on_connect(client, userdata, flags, rc):
    print("連線結果：" + str(rc))
    #訂閱主題
    client.subscribe(SubTopic1)
    
#設定訂閱更新時的Callback
def on_message(client, userdata, msg):
    f = open('receive.jpg','wb+') #開啟檔案
    f.write(msg.payload)#寫入檔案
    print('image received and process the hand tracker')
    f.close()#關閉檔案
    
    #設定視窗名稱及型態
    cv2.namedWindow('MediaPipe', cv2.WINDOW_NORMAL)
    
    #顯示影像檔
    img=cv2.imread('receive.jpg')
    # img1=cv2.resize(img,(640,480))
    #target=0 #'city.mp4'
    #target=img
    
    #cap=cv2.VideoCapture(target)
    
    #st=time.time()  
    frame = img.copy()
        
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(image)
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(
                image=frame,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_IRISES,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing_styles
                .get_default_face_mesh_iris_connections_style())
            
    cv2.imshow('MediaPipe', frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        exit()
    print("quit the hand process window")
        
 
#設定Mqtt連線    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MqttBroker, MqttPort, 60)
#等候訂閱
client.loop_forever()