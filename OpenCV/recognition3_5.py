import cv2
import mediapipe as mp
import paho.mqtt.client as mqtt


conn = mp.solutions.pose.POSE_CONNECTIONS
pose = mp.solutions.pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils
spec = mp.solutions.drawing_styles.get_default_pose_landmarks_style()
# spec = mp_drawing.DrawingSpec(color=(255, 255, 255),thickness=3, circle_radius=1)

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
    print('image received and process the pose tracker')
    f.close()#關閉檔案
        
    #顯示影像檔
    img=cv2.imread('receive.jpg')
    if img is None:
        print("Failed to read received image.")
        return

    # img=cv2.resize(img,(800,600))
    frame = img.copy()

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, conn, spec)
    cv2.imshow('MediaPipe Pose', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        client.loop_stop() # 使用更優雅的方式停止 MQTT 迴圈

# --- Code Review and Suggestions ---
# 1. 將視窗建立移至主程式，避免每次收到訊息都重新建立視窗
cv2.namedWindow('MediaPipe Pose', cv2.WINDOW_NORMAL)
#設定Mqtt連線    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MqttBroker, MqttPort, 60)
#等候訂閱
client.loop_forever()
cv2.destroyAllWindows()