from turtle import *
from random import *

# Flytter skilpadden til tilfeldig posisjon
def moveToRandomLocation():
    penup()
    setpos(randint(-400, 400), randint(-400, 400))
    pendown()

# Tegner en stjerne i en bestemt størrelse
def drawStar(starSize, starColour):
    color(starColour)
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(starSize)
    end_fill()
    penup()

# Funksjon for å tegne en liten galakse med stjerner
def drawGalaxy(numberOfStars):
    starColours = ["#058396","#0275A6","#827E01"]
    moveToRandomLocation()
    # Tegner mange små fargede stjerner
    for star in range(numberOfStars):
        penup()
        left(randint(-180, 180))
        forward(randint(5, 20))
        pendown()
        # Tegner en liten stjerne i tilfeldig farge
        drawStar(2, choice(starColours))
        
# Funksjon for å tegne stjernebilder!
def drawConstellation(numberOfStars):
    moveToRandomLocation()
    # Først tegner vi alle stjernene untatt den siste
    # Hengende i linjer som dette *--*--*--
    for star in range(numberOfStars-1):
        drawStar(randint(7, 15), "White")
        pendown()
        left(randint(-90, 90))
        forward(randint(30, 70))
    # Tegner den siste stjernen
    drawStar(randint(7, 15), "White")


speed(11)

# mørkeblå bakgrunn
bgcolor("#06011c")

# Tegner 30 stjerner med tilfeldig størrelse og posisjon
for star in range(30):
    moveToRandomLocation()
    drawStar(randint(5, 25) , "White")

# Tegner 3 små galakser med 40 stjerner
for galaxy in range(3):
    drawGalaxy(40)

# Tegner 2 stjernetegn, begge med tilfeldige nummere av stjerner
for constellation in range(2):
    drawConstellation(randint(4, 7))

hideturtle()
done()









#def drawPlanet(planetSize, planetColor):
