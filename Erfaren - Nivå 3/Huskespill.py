import random

def legg_til_tilfeldig_ord(liste):
    ordliste = ['eple', 'banan', 'appelsin', 'melon', 'jordbær', 'ananas']
    tilfeldig_ord = random.choice(ordliste)
    liste.append(tilfeldig_ord)
    return liste

def lag_liste(tekst):
    liste = tekst.split("-")
    return liste

min_liste = []
spill_i_gang = True
antall_runder = 0

while spill_i_gang:
    antall_runder += 1
    print("Runde", antall_runder)
    legg_til_tilfeldig_ord(min_liste)
    print("Memoriser følgende ord:", "-".join(min_liste))
    input("Trykk Enter for å fortsette...")
    print("\n" * 50)  # for å skjule listen
    gjettet_liste = lag_liste(input("Skriv inn ordene du husker, separert med - : "))
    if gjettet_liste == min_liste:
        print("Du husket riktig!")
    else:
        print("Feil rekkefølge, spillet er over.")
        print("Du klarte å huske", len(min_liste), "ord etter hverandre.")
        spill_i_gang = False

#if antall_runder == "0":
 #   print(input("Trykk Enter for å fortsette...")

#tom_liste = []

#score = len(tom_liste)

#def legg_til_tilfeldig_ord(liste):
 #   ordliste = ["Andreas", "Ingrid", "UFO", "AI", "Python"]
 #   tilfeldig_ord = random.choice(ordliste)
  #  liste.append(tilfeldig_ord)
  #  return liste


#min_liste = []
#utvidet_liste = legg_til_tilfeldig_ord(min_liste)
#print(utvidet_liste)

#print("Klikk ENTER når du er klar til å huske")

#def lag_liste(tekst):
#    liste = tekst.split("-")
#    return liste









    #print("Gratulerer du husket: " + str(score) + " ord på rad!")



#tekst = input('Skriv inn ordene i riktig rekkefølge, skill dem med bindestrek "-"')

#def tekst_til_liste():
    
