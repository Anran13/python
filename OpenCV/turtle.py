# package turtle

#================================================
import turtle
turtle.bgcolor('yellow')

mypen = turtle.Pen()
mypen.speed(0)

cnt = 8
while True:
    for i in range(9):
        mypen.right(1)
        mypen.forward(20)
    
    for i in range(26):
        mypen.right(8)
        mypen.forward(10)
    
    for i in range(9):
        mypen.right(1)
        mypen.forward(20)

    mypen.right(360/cnt)

turtle.done()

#================================================
import turtle 
import cv2
turtle.getscreen().colormode(255)
img1 = cv2.imread('C:/image_name.png')[0:-2:2]

width = len(img1[0])
# height = len(img1[1])
height = len(img1)
# print(width)
# print(height)
turtle.setup(width=width/2 + 100, height=height)

turtle.penup()
turtle.goto(-width / 4 + 10, height / 2 - 10)
turtle.pendown()
turtle.tracer(2000)
for k1, i in enumerate(img1):
    for j in i[::2]:
        turtle.pencolor(j[0], j[1], j[2])
        # turtle.pencolor(0, 255,0)
        turtle.right(1)
        turtle.forward(3)
        # turtle.forward(1)
    turtle.penup()
    turtle.goto(-width / 4 + 10, height / 2 - 10 - k1 -1)
    turtle.pendown()
turtle.done()
