from random import randint

ant_stykker = 5
ant_rett = 0

for i in range(ant_stykker):
    tall1 = randint(2, 12)
    tall2 = randint(2, 12)

    print("Hva er " + str(tall1) + " ganger " + str(tall2) + "?")

    svar = input()

    if int(svar) == tall1 * tall2:
        print("Ja, svaret er " + svar)
        ant_rett = ant_rett + 1
    else:
        print("Nei, det riktige svaret er " + str(tall1 * tall2))


print("Du fikk " + str(ant_rett) + " av " + str(ant_stykker) + " riktige")





