from hashlib import sha256

def hash(data):
     h = sha256()
     h.update(data.encode())
     return h.hexdigest()

secret = 17
message = "yvååc kcfåu"

def mac(key, message):
    return (message, hash(str(key) + message))

def verify_mac(key, message, mac):
    if mac == hash(str(key) + message):
        return "Alt ok"
    else:
        return "Noen har tuklet med meldingen!"

# Sende hemmlig melding til mottaker med hash-funksjon
#1. mac(secret, message)
#2. verify_mac(secret, 'yvååc kcfåu', 'b5a1c943bf39423f55a6fa4e43a7642feddd371c355ec4560b2f360a2634d244')

