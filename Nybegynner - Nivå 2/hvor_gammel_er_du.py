print("Hei, jeg er en datamaskin.")
print("Jeg er derfor kjempeflink i matematikk.")
print("Skal jeg vise deg?")


år = 2023
født = int(input("Skriv året du er født: "))

alder = år - født
alder_str = str(alder)
print("Jeg regnet ut at alderen din er: " + alder_str)


tekst = str(input("Stemmer det at du er så gammel? ")).lower()


if tekst == "ja":
    print("Der ser du, jeg er kjempeflink i matematikk!")
else:
    ny_alder = alder - 1
    p_alder = str(ny_alder)
    print("Viste at du var " + p_alder + " år")
