alphabet = "abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
l = len(alphabet)

def encode(letter, key):
    pos = alphabet.find(letter)

    newpos = (pos + key) % l

    return alphabet[newpos]


def decode(letter, key):
    pos = alphabet.find(letter)

    newpos = (pos - key) % l

    return alphabet[newpos]

#print(encode("u", 18))
#print(decode("j", 18))


def encrypt(message, key):
    output = ""

    for character in message:
        if character in alphabet:
            output = output + encode(character, key)
        else:
            output = output + character

    print(output)

encrypt("Jeg elsker lillebæ og vennene hans!", 18)

#key = 18
#message = "Jeg elsker lillebæ og vennene hans!"



def decrypt(secretmessage, key):
    output = ""

    for character in secretmessage:
        if character in alphabet:
            output = output + decode(character, key)
        else:
            output = output + character

    print(output)

decrypt("Øwy wAHåwG AæAAwtP Dy KwCCwCw zsCH!", 18)

#key = 37
#message = "qMOHPIZHQSSMHØQLHØQTHgHORfZMHTMSÆMZHNWZLQHRMOHMZHWXXØIØØHUMLHgHSWLM"


