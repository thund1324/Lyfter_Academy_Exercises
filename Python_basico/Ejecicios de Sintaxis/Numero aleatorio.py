import random

secret = random.randint(1, 10)
number = 0

while number != secret:
    number = int(input("Adivina el número (1-10): "))

    if number == secret:
        print("Adivinaste el número.")
        break
    print("Incorrecto, intenta de nuevo.")

