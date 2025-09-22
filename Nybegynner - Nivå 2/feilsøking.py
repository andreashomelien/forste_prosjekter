# Et program for å sortere 4 navn etter lengde
navn = []                                          # Definerer 'navn' som en tom liste
x = 1                                              # Sier at det skal skje en forandring
for t in range(1,5):                               # Gjentar løkken 4 ganger
    svar = input("Legg til et navn: ")             # Ber om et navn
    navn.append(svar)                              # Legger navnet til i listen 'navn'.
while x == 1:                                      # Gjentar løkken så lenge det gjøres forandringer
    for s in range(4):                             # Gjentas 4 ganger, en gang for hvert navn
        x = 0                                      # Sier at det ikke er gjort noen forandringer inne i løkken ennå
        for t in range(3):                         # Gjenta 3 ganger, for å kunne flytte lange navn oppover i lista
           if len(navn[t]) > len(navn[t+1]):       # Flytt lange navn fremover i lista
              bytte = navn[t]                      # Legger det første navnet i en tom variabel
              navn[t] = navn[t+1]                  # Gjør det første navnet likt som det andre
              navn[t+1] = bytte                    # Lar det andre navnet bli likt som det første var
              x = 1                                # Sier at det er gjort en forandring

for i in range(0, len(navn)):
    print("Navnene sortert etter lengde:" , navn[i])      # Skriver ut hele lista


