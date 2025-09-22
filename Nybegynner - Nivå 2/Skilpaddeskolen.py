from turtle import *
speed(11)
shape("turtle")

#def poly(sides, lenght): #Vi lager funksjonen
    #angle = 360 / sides

    #for n in range(sides):
        #forward(lenght)
        #right(angle)

#pencolor("green")
#poly(4, 100) # Vi kaller på funksjonen
#right(180)
#pencolor("blue")
#poly(3, 150)

#lenght = 200
#for num in range(8):
    #forward(lenght/16)
    #penup()
    #forward(lenght/16)
    #pendown()

def dashforward(lenght):
    for num in range(8):   
        forward(lenght/16)
        penup()
        forward(lenght/16)
        pendown()
        
def dashpoly(sides, lenght):
    angle = 360/sides

    for n in range(sides):
        dashforward(lenght)
        right(angle)
        

pencolor("red")
dashpoly(4, 100)
right(180)
pencolor("blue")
dashpoly(3, 150)


