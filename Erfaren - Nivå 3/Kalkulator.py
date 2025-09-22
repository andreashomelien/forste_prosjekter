def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

def subtract(a, b):
    result = a - b
    print(f"{a} - {b} = {result}")

def multiply(a, b):
    result = a * b
    print(f"{a} * {b} = {result}")

def divide(a, b):
    if b == 0:
        print("Kan ikke dele på 0!")
    else:
        result = a / b
        print(f"{a} / {b} = {result}")

def opphøyd(a, b):
    result = a ** b
    print(f"{a} ** {b} = {result}")


num_calculations = int(input("Hvor mange beregninger vil du gjøre? "))
for i in range(num_calculations):
    operator = input("Operator +, -, *, /, **: ")
    a = float(input("First number: ")) #first_num
    b = float(input("Second number: ")) #second_num


    if operator == "+":
        add(a, b)
    elif operator == "-":
        subtract(a, b)
    elif operator == "*":
        multiply(a, b)
    elif operator == "/":
        divide(a, b)
    elif operator == "**":
        opphøyd(a, b)
    else:
        print("Ugyldig operatør!")

    print() #legger til et blankt linjeskift mellom beregningene
