# process image
# package cv2
import cv2

# image source: https://pixabay.com/vectors/astronaut-night-sky-star-7059915/

#=================================================================================
img = cv2.imread('C:/Users/ROG/Downloads/astronaut_pixabay.png')
#=================================================================================
# image property
img = cv2.imread("C:/Users/ROG/Downloads/astronaut_pixabay.png")   
print("image property")
print(f"shape = {img.shape}")
print(f"size  = {img.size}")
print(f"dtype = {img.dtype}")
print(f"BGR = {img[100,100]}")
print(f"BGR = {img[100,100,0]}, {img[100,100,1]}, {img[100,100,2]}")

#================================================
# change to grey scale
img = cv2.imread('C:/Users/ROG/Downloads/astronaut_pixabay.png', cv2.IMREAD_GRAYSCALE)
cv2.imwrite("C:/Users/ROG/Downloads/astronaut_pixabay_grey.png", img)
cv2.imshow('grey', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#================================================
# chane BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
cv2.imshow('image_rgb', image_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
# transform to 2-dim
pixels = img_rgb.reshape(-1, 3)
# find different colors
unique_colors = np.unique(pixels, axis=0)
print(f"圖片中不同顏色數量：{len(unique_colors)}")
print("部分顏色範例：", unique_colors[10])

#================================================
# add rectangle area
cv2.imshow("Before the change", img)
for y in range(img.shape[0]-350, img.shape[0]-300):
    for x in range(img.shape[1]-150, img.shape[1]-100):
        img[y, x] = [0, 0, 255]
cv2.imshow("After the change", img)
cv2.imwrite("C:/Users/Downloads/astronaut_pixabay_change.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#================================================
# resize the image
try:
    img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
    cv2.imwrite("C:/Users/Downloads/astronaut_pixabay_resize.png", img)
    cv2.imshow('img1', img)
    cv2.waitKey(0)
    cv2.destroyAllWindos()
except:
    print("Can't find the image!")

#================================================
# [B G R]
rows = 300
cols = 300
img = np.zeros((rows, cols, 3), np.uint8)
for row in range(rows):
    for col in range(cols):
        img[row][col] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
cv2.imwrite("C:/Users/Downloads/mosaic.png", img)
cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#================================================
img = np.zeros((500, 500, 3), dtype='uint8')
print(img)
img[150:350, 150:350] = [0,0,255]
print(img[150:350, 150:350])
# print(img.size)
# cv2.imwrite("test1.jpg", img)
cv2.imshow("test1", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#================================================
print(img.shape)
print(img.shape[1])
for row in range(img.shape[0]-300, img.shape[0]-265):
    for col in range(img.shape[1]):
        img[row][col] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
cv2.imwrite("C:/Users/Downloads/astronaut_pixabay_mosaic.png", img)
cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#================================================
img = np.zeros((600, 600), np.uint8)
cv2.rectangle(img, (0,0), (400, 200), (255,0,0), cv2.FILLED)
cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (255,0,0), 5)
cv2.circle(img, (300, 400), 30, (255,0,0), cv2.FILLED)
cv2.putText(img, 'Hello', (100, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
cv2.imwrite("C:/Users/Downloads/hello.png", img)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#================================================
cv2.imshow("BGR Color Space", img)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # BGR轉HSV
cv2.imwrite("C:/Users/Downloads/astronaut_pixabay_hsv.png", img_hsv)
cv2.imshow("HSV Color Space", img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

#================================================
# # 目標顏色BGR
target_color = np.array(unique_colors[100])

# 設定顏色範圍，因為像素值可能有微小差異，設定±範圍
lower = target_color - np.array([50, 50, 50])  # 下界
upper = target_color + np.array([50, 50, 50])  # 上界

# 確保範圍在0~255之間
lower = np.clip(lower, 0, 255)
upper = np.clip(upper, 0, 255)

# 產生遮罩，找出符合顏色範圍的像素
mask = cv2.inRange(img, lower, upper)

# 找出符合顏色的像素座標 (y, x)
positions = np.column_stack(np.where(mask > 0))

print(f"找到 {len(positions)} 個符合顏色 {target_color} 的像素位置")
print("部分座標範例：", positions[:10])

# 如果想在圖片上標記這些位置，可以用以下方式
for (y, x) in positions:
    cv2.circle(img, (x, y), 1, (0, 0, 255), -1)  # 用紅點標記

cv2.imshow('Marked Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("C:/Users/Downloads/astronaut_pixabay_mark.png", img)

#================================================
# spit into blue, green, red
cv2.imshow('bgr', img)
blue, green, red = cv2.split(img)
cv2.imwrite("C:/Users/Downloads/astronaut_pixabay_split_blue.png", blue)
cv2.imwrite("C:/Users/Downloads/astronaut_pixabay_split_green.png", green)
cv2.imwrite("C:/Users/Downloads/astronaut_pixabay_split_red.png", red)
# cv2.imshow('blue', blue)
# cv2.imshow('green', green)
# cv2.imshow('red', red)

print(f"BGR  影像 : {img.shape}")
print(f"B通道影像 : {blue.shape}")
print(f"G通道影像 : {green.shape}")
print(f"R通道影像 : {red.shape}")

# merge to the origin image
bgr_image = cv2.merge([blue, green, red])   # 依據 B G R 順序合併
cv2.imshow("B -> G -> R ", bgr_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

#================================================
hsv_image = img = cv2.imread('C:/Users/Downloads/astronaut_pixabay_hsv.png')
hue, saturation, value = cv2.split(hsv_image)

cv2.imshow("The HSV Image", hsv_image)
cv2.imwrite("C:/Users/Downloads/astronaut_pixabay_hsv_hue.png", hue)
cv2.imwrite("C:/Users/Downloads/astronaut_pixabay_hsv_sat.png", saturation)
cv2.imwrite("C:/Users/Downloads/astronaut_pixabay_hsv_val.png", value)

cv2.imshow('hsv', hue)
cv2.imshow('saturation', saturation)
cv2.imshow('value', value)

hsv_image = cv2.merge([hue, saturation, value])   # 依據 H S V 順序合併
cv2.imshow("The Merge Image", hsv_image)

# hue.fill(200) # hue[:,:] = 200
# saturation.fill(255)
value.fill(255)
hsv_image = cv2.merge([hue, saturation, value])
cv2.imshow("The Merge Image - sat = 200", hsv_image)

new_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR) # HSV 轉 BGR
cv2.imshow("The New Image", new_image)

# cv2.imwrite("C:/Users/Downloads/astronaut_pixabay_hsv_hue_200_merge.png", hsv_image)
# cv2.imwrite("C:/Users/Downloads/astronaut_pixabay_hsv_sat_255_merge.png", hsv_image)
cv2.imwrite("C:/Users/Downloads/astronaut_pixabay_hsv_val_255_merge.png", hsv_image)

# cv2.imwrite("C:/Users/Downloads/astronaut_pixabay_hsv_hue_200_rgb.png", new_image)
# cv2.imwrite("C:/Users/Downloads/astronaut_pixabay_hsv_sat_255_rgb.png", new_image)
cv2.imwrite("C:/Users/Downloads/astronaut_pixabay_hsv_val_255_rgb.png", new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

#================================================
img = cv2.resize(img, (0,0), fx=0.4, fy=0.4)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img, (15,15), 10)
canny = cv2.Canny(img, 100, 130)
cv2.imwrite("C:/Users/Downloads/astronaut_pixabay_canny.png", canny)

kernel1 = np.ones((100,100), np.uint8)
dilate = cv2.dilate(canny, kernel1, iterations=5)

kernel2 = np.ones((1,1), np.uint8)
erode = cv2.erode(dilate, kernel2, iterations=1)
cv2.imshow('img', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

#================================================
img = cv2.resize(img, (0, 0), fx=0.4, fy=0.4)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar", 640, 320)

def empty(v):
    pass

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
        cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 4)

        if corners == 3:
            cv2.putText(imgContour, 'tiangle', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif corners == 4:
            cv2.putText(imgContour, 'rectangle', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif corners == 5:
            cv2.putText(imgContour, 'pentagon', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif corners >= 6:
            cv2.putText(imgContour, 'circle', (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imwrite("C:/Users/Downloads/astronaut_pixabay_contour.png", imgContour)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.imshow('canny', canny)
cv2.waitKey(0)

cv2.imshow('imgContour', imgContour)
cv2.waitKey(0)