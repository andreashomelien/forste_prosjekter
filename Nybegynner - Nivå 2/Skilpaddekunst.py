from turtle import *

shape("turtle")
shapesize(2)
bgcolor("#008080")
color("#00FF7F")
speed(11)

#sides = 10
#lenght = 100
#angle = 360 / sides

def polygon(sides, length):
    angle = 360 / sides

    for i in range(sides):
        forward(length)
        right(angle)

#polygon(4, 100)



def polylines(sides, lenght, angle):
    for i in range(sides):
        forward(lenght)
        right(angle)


#polylines(5, 100, 144)
#polylines(91, 200, 91)

def spiral(sides, lenght, angle):
    for i in range(sides):
        forward(lenght)
        right(angle)
        lenght = lenght + 5

#spiral(100, 5, 125)
#spiral(100, 10, 90)
spiral(100, 10, 60)




