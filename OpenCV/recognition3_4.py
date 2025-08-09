import mediapipe as mp
import cv2,time
import paho.mqtt.client as mqtt

# 開啟畫關鍵點與face mesh網格功能
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
mp_drawing_styles = mp.solutions.drawing_styles
# 載入嘴唇的透明背景圖片
mouth_normal = cv2.imread("image/lip.png")
# 設定正確率
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing_styles = mp.solutions.drawing_styles

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
    # 先找出畫面的長寬大小
    h, w, d = frame.shape   
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(image)
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(
                image=frame,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing_styles
                .get_default_face_mesh_tesselation_style())
            # 點0與17分別是嘴唇上下的座標，取得嘴唇大小
            mouth_len = int((face_landmarks.landmark[17].y * h)-int(face_landmarks.landmark[0].y * h))
            # 將嘴唇圖案的圖片轉換成適合的大小
            mouth = cv2.resize(mouth_normal, (mouth_len * 3, mouth_len))
            # 將嘴唇圖案轉灰階
            mouth_gray = cv2.cvtColor(mouth, cv2.COLOR_BGR2GRAY)
            # 將嘴唇圖案去背
            _, mouth_mask = cv2.threshold(mouth_gray, 25, 255, cv2.THRESH_BINARY_INV)
            # 找出嘴唇的高度img_height 與寬度img_width
            img_height, img_width, _ = mouth.shape
            # 點13與14的中間是嘴唇的中心點，找出放圖的左上角落座標
            x, y = int(face_landmarks.landmark[13].x * w - img_width/2), \
                   int(((face_landmarks.landmark[13].y + face_landmarks.landmark[14].y)/2) * h - img_height/2)
            # 將去背圖案與真的人嘴唇合併成一矩形 mouth
            mouth_area = frame[y: y + img_height, x: x + img_width]
            mouth_area_no_mouth = cv2.bitwise_and(mouth_area, mouth_area, mask=mouth_mask)
            mouth = cv2.add(mouth_area_no_mouth, mouth)
            # 在點(x, y)放上圖案mouth
            frame[y: y+img_height, x: x+img_width] = mouth
            
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