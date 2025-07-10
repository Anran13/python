# process image
# package cv2

#================================================
import cv2
img = cv2.imread('C:/Users/python.png')
cv2.imshow('img1', img)
cv2.waitKey(0)

#================================================
img = cv2.imread('C:/Users/python.png', cv2.IMREAD_GRAYSCALE)
try:
    cv2.imshow('img1', img)
    cv2.waitKey(0)
    cv2.destroyAllWindos()
except:
    print("Can't find the image!")

#================================================
img = cv2.imread('C:/Users/python.png', cv2.IMREAD_GRAYSCALE)
try:
    img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
    cv2.imwrite("C:/Users/python2.png", img)
    cv2.imshow('img1', img)
    cv2.waitKey(0)
    cv2.destroyAllWindos()
except:
    print("Can't find the image!")

#================================================
import numpy as np
import random
img = cv2.imread('C:/Users/python2.png')
print(img) 
print(img.shape)
# [B G R]
rows = 300
cols = 300
img = np.zeros((rows, cols, 3), np.uint8)
for row in range(rows):
    for col in range(cols):
        img[row][col] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#================================================
img = np.zeros((500, 500, 3), dtype='uint8')
print(img)
img[150:350, 150:350] = [0,0,255]
print(img[150:350, 150:350])
# print(img.size)
cv2.imwrite("test1.jpg", img)
cv2.imshow("test1", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#================================================
img = cv2.imread('C:/Users/python2.png')
print(img.shape)
print(img.shape[1])
for row in range(img.shape[0]-300, img.shape[0]-265):
    for col in range(img.shape[1]):
        img[row][col] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
cv2.imwrite("C:/Users/python3.png", img)
cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#================================================
img = cv2.imread('C:/Users/python1.png')
img = cv2.resize(img, (0,0), fx=0.4, fy=0.4)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img, (15,15), 10)
canny = cv2.Canny(img, 100, 130)
cv2.imwrite("C:/User/python4.png", canny)

kernel1 = np.ones((100,100), np.uint8)
dilate = cv2.dilate(canny, kernel1, iterations=5)

kernel2 = np.ones((1,1), np.uint8)
erode = cv2.erode(dilate, kernel2, iterations=1)
cv2.imshow('img', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

#================================================
img = np.zeros((600, 600), np.uint8)
cv2.rectangle(img, (0,0), (400, 200), (255,0,0), cv2.FILLED)
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (255,0,0), 5)
cv2.circle(img, (300, 400), 30, (255,0,0), cv2.FILLED)
cv2.putText(img, 'Hello', (100, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#================================================
import cv2
import numpy as np

def empty(v):
    pass

img = cv2.imread('C:/Users/ROG/Desktop/PYImage_250621/image/image1.png')
img = cv2.resize(img, (0, 0), fx=0.4, fy=0.4)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar", 640, 320)

cv2.createTrackbar("Hue Min", "TrackBar", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBar", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBar", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBar", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBar", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBar", 255, 255, empty)

while True:
    h_min = cv2.getTrackbarPos('Hue Min', 'TrackBar')
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBar')
    s_min = cv2.getTrackbarPos('Sat Min', 'TrackBar')
    s_max = cv2.getTrackbarPos('Sat Max', 'TrackBar')
    v_min = cv2.getTrackbarPos('Val Min', 'TrackBar')
    v_max = cv2.getTrackbarPos('Val Max', 'TrackBar')
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, upper)
    cv2.imshow('img', img)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    cv2.waitKey(1)


cv2.imshow('img', img)
cv2.imshow('hsv', hsv)
cv2.waitKey(0)

cv2.destroyAllWindows()

#================================================
img = cv2.imread('C:/Users/python2.png')
imgContour = img.copy()
canny = cv2.Canny(img, 150, 200)

contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for cnt in contours:
    # print(cnt)
    cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 4)
    area = cv2.contourArea(cnt)
    # print(area)
    if area > 100 and area < 150:
        peri = cv2.arcLength(cnt, True)
        # print(peri)
        vertices = cv2.approxPolyDP(cnt, peri * 0.02, True)
        # print(len(vertices))
        corners = len(vertices)
        
        x, y, w, h = cv2.boundingRect(vertices)
        cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0,255,0), 4)

        if corners == 3:
            cv2.putText(imgContour, 'tiangle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        elif corners == 4:
            cv2.putText(imgContour, 'rectangle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        elif corners == 5:
            cv2.putText(imgContour, 'pentagon', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        elif corners >= 6:
            cv2.putText(imgContour, 'circle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.imshow('canny', canny)
cv2.waitKey(0)
cv2.imwrite("C:/Users/python6.png", imgContour)
cv2.imwrite("C:/Users/python7.png", imgContour)

cv2.imshow('imgContour', imgContour)
cv2.waitKey(0)

