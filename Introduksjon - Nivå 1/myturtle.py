#Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.

from turtle import *

speed(1)
shape("turtle")

sides = 10
lenght = 100

fillcolor("#009E60")
pencolor("#009E60")
begin_fill()

angle = 360/sides
for count in range(sides):
    forward(lenght)
    right(angle)
end_fill()

