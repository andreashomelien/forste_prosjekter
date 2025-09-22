def verify_barcode(digits):
#EAN-13 strekkode verdifiserer
    

    # Regn ut i henhold til formelen
    summert = 3 * (digits[1] + digits[3] + digits[5] + digits[7]
               + digits[9] + digits[11])
    print(summert)
    summert = summert + (digits[0] + digits[2] + digits[4] + digits[6]
                 + digits[8] + digits[10])

    # Finn differansen mellom 10 og det siste sifferet i summen
    # Sjekksifferet kan ikke være 10, så den siste % 10 gjør at det
    # blir 0 i stedet.
    checksum = (10 - (summert % 10)) % 10

    if checksum == digits[12]:
        return True
    else:
        return False

#check - verify_barcode([7,0,3,8,0,1,0,0,0,1,9,1,8])
#check - verify_barcode([9,7,8,0,0,6,2,7,3,1,0,2,9])

def interpret_barcode(barcode):

    # Vi sjekker først at vi faktisk har fått nøyaktig 13 sifre
    if (len(barcode) != 13) or not (barcode.isdigit()):
        return None
    # Oversett teksten til en liste av sifre
    digits = [int(d) for d in barcode]

    return digits

#check - verify_barcode(interpret_barcode("9780062731029"))
    

    















