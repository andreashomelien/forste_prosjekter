from random import *

#seed("lillebæ")

#for i in range(100):
    #print(randint(0, 1000))

# over er det brukt "randint" ikke sikkert


# under er det brukt "randbelow" fra secrets bibloteket = sikkert

from secrets import *

seed("Lillebæ")

for i in range(100):
    print(randbelow(1001))


