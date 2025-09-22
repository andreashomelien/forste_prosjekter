alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'æ', 'ø', 'å', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'æ', 'ø', 'å']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Her er ditt {cipher_direction}d resultat: {end_text}")


from art import logo

print(logo)

should_end = False
while not should_end:

    direction = input("Skriv 'encode' for å kryptere, skriv 'decode' for å dekryptere:\n")
    text = input("Skriv din melding:\n").lower()
    shift = int(input("Skriv din hemmelige nøkkel:\n"))
    shift = shift % 29

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Skriv 'ja' hvis du vil prøve igjen. Ellers skriv 'nei'.\n")
    if restart == "nei":
        should_end = True
        print("Ha det bra!")


