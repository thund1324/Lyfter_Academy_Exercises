top = 0

for count in range(0, 3):
    number = int(input("Ingrese el número: "))

    if number > top:
        top = number

print("El número más grande es:", top)