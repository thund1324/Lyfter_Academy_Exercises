first_list = [22, 6, 57, 8, 19, 8, 4, 3, 9, 10, 57, 8, 6, 4, 3, 9, 10, 57, 8, 6, 4, 65, 9, 1]

number = int(input("Ingrese un numero: "))
repeat = 0

for i in range(len(first_list)):
    if first_list[i] == number:
        repeat += 1

print(f"El numero {number} se repite {repeat} veces en la lista.")