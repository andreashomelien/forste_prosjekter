from random import randint

rand_number = randint(1, 100)
tall = 0

#print(rand_number)

guess = 1
while tall != rand_number:
    tall = int(input("Skriv et tall: "))
    if tall > rand_number:
        print("Lower!")
        guess = guess + 1
    elif tall < rand_number:
        print("Higher!")
        guess = guess + 1
    else:
        print("Correct!")
        print("You guessed: " + str(guess) + " times!")

        
