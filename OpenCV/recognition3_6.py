import mediapipe as mp
import cv2,time
import paho.mqtt.client as mqtt

import numpy as np
import math

pose = mp.solutions.pose.Pose()
conn = mp.solutions.pose.POSE_CONNECTIONS
mp_drawing = mp.solutions.drawing_utils
spec = mp.solutions.drawing_styles.get_default_pose_landmarks_style()
# switch, count = 0, 0
# color = (0,0,255)


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
    switch, count = 0, 0
    color = (0,0,255)
    f = open('receive.jpg','wb+') #開啟檔案
    f.write(msg.payload)#寫入檔案
    print('image received and process the hand tracker')
    f.close()#關閉檔案
    
    #設定視窗名稱及型態
    cv2.namedWindow('MediaPipe', cv2.WINDOW_NORMAL)
    
    #顯示影像檔
    img=cv2.imread('receive.jpg')
    img=cv2.resize(img,(1200,1000))
    frame = img.copy()
        
    # image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # results = face_mesh.process(image)
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    h, w, c = frame.shape
    xx1 = int(w * 0.1)
    poslist = []
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, conn, spec)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            cx, cy = int(lm.x * w), int(lm.y * h)
            poslist.append([id, cx, cy])
    try:
        # 右手肘的角度
        x1, y1 = poslist[12][1], poslist[12][2]
        x2, y2 = poslist[14][1], poslist[14][2]
        x3, y3 = poslist[16][1], poslist[16][2]
        right_angle = abs(int(math.degrees(math.atan2(y1 - y2, x1 - x2) - math.atan2(y3 - y2, x3 - x2))))
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 255), 3)
        cv2.line(frame, (x3, y3), (x2, y2), (0, 255, 255), 3)
        cv2.circle(frame, (x1, y1), 10, (0, 255, 255), cv2.FILLED)
        cv2.circle(frame, (x1, y1), 15, (0, 255, 255), 2)
        cv2.circle(frame, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
        cv2.circle(frame, (x2, y2), 15, (0, 0, 255), 2)
        cv2.circle(frame, (x3, y3), 10, (0, 255, 255), cv2.FILLED)
        cv2.circle(frame, (x3, y3), 15, (0, 255, 255), 2)
        # 以10到170度 來計算右手彎曲的程度，最高%=100，最低%=0
        right_per = np.interp(right_angle, (10, 170), (100, 0))
        # 根據右手彎曲程度計算bar的高度 Y軸座標，最高y=200，最低y=400
        right_bar = int(np.interp(right_angle, (10, 170), (200, 400)))
        # 畫矩形來代表bar的高度， 同時印出數字
        cv2.rectangle(frame, (xx1, int(right_bar)), (xx1 + 30, 400), color, cv2.FILLED)
        cv2.putText(frame, str(int(right_per)) + '%', (xx1 - 10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        # 手起到95%或5%算半個
        color = (0, 0, 255)
        
        if right_per >= 70:
            color = (0, 255, 0)
            if switch == 0:
                count += 0.5
                switch = 1
        if right_per <= 30:
            color = (0, 255, 0)
            if switch == 1:
                count += 0.5
                switch = 0
    except:
        pass
    cv2.putText(frame, str(count), (xx1 - 40, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)
            
    cv2.imshow('MediaPipe', frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        
        print("quit the hand process window")
        exit()
        
 
#設定Mqtt連線    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MqttBroker, MqttPort, 60)
#等候訂閱
client.loop_forever()