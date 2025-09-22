from random import choice

word = choice(["kode", "kurs", "robot", "klubb", "python", "konge"])

guessed = []
wrong = []

tries = 7

while tries > 0:
    out = ""
    for letter in word:
        if letter in guessed:
            out = out + letter
        else:
            out = out + "_"

    if out == word:
        #print("Du gjettet", word)
        break

    print("Gjett en bokstav i ordet:", out)
    print(tries, "forsøk igjen")
    
    guess = input().lower()

    if guess in guessed or guess in wrong:
        print("Bokstaven er allerede gjettet på:", guess)
    elif guess in word:
        print("Yay")
        guessed.append(guess)
    else:
        print("Nope")
        tries = tries - 1
        wrong.append(guess)

    print()

if tries:
    print("Du gjettet", word)
else:
    print("Du klarte ikke å gjette", word)


