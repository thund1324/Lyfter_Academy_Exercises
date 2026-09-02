first_list = []
total = 0
note = 0
flag = True

while flag == True:
    number = int(input("Ingrese un numero: "))
    first_list.append(number)
    total += number
    note += 1

    option = input("Ingresar otro numero? (y/n): ")
    if option == "n":
        flag = False

total = total / note

print(f"El promedio de nota es: {total}")

uppers = []

for i in range(len(first_list)):
    if first_list[i] > total:
        uppers.append(first_list[i])

print(f"Los numeros mayores al promedio son: {uppers}")
