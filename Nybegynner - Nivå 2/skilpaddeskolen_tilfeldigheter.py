from turtle import *
from random import randrange, choice
colors = ["red", "blue", "green"]
shape("turtle")
speed(11)
pensize(2)


def poly(sides, lenght):
    angle = 360 / sides

    for n in range(sides):
        forward(lenght)
        right(angle)

for count in range(10):
    pencolor(choice(colors))
    right(randrange(0, 360))
    poly(randrange(3, 9), randrange(10, 30))
