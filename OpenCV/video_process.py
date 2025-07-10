# package cv2
import cv2

#================================================
cap = cv2.VideoCapture("C:/Users/video_name.mp4")
if not cap.isOpened():
    print("Cannot open the video!")
    exit()
else:
    print("Open now!")

#================================================
cap = cv2.VideoCapture("C:/Users/video_name.mp4")
if not cap.isOpened():
    print("Cannot open the video!")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    cv2.imshow('video', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

#================================================
cap = cv2.VideoCapture("C:/Users/video_name.mp4")
if not cap.isOpened():
    print("Cannot open the video!")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    frame = cv2.resize(frame, (0,0), fx=0.4, fy=0.4)
    cv2.imshow('video', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

#================================================
cap = cv2.VideoCapture("C:/Users/video_name.mp4")
if not cap.isOpened():
    print("Cannot open the video!")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('video', gray)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

#================================================
url = 'https://cctv4.kctmc.nat.gov.tw/0d6724a3/&t=1751081023623'
cap = cv2.VideoCapture(url)        

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # read every frame of the video
    ret, frame = cap.read()            
    if not ret:
        # if cannot read, then print error message.
        print("Cannot receive frame")  
        # streaming interval might be breaking up, so continue read the frame
        cap = cv2.VideoCapture(url)     
        continue
    frame = cv2.resize(frame, (0, 0), fx=3, fy=3)
    cv2.imshow('oxxostudio', frame)
    # stop when pressing "q"     
    if cv2.waitKey(1) == ord('q'):     
        break
# release resources
cap.release()                           
cv2.destroyAllWindows()

