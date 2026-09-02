upper = 0
first_list = []
for i in range(0, 10):
    number = int(input("Ingrese un número: "))
    if number > upper:
        upper = number
    first_list.append(number)

print(f"Números ingresados: {first_list}")
print(f"El número más alto es: {upper}")