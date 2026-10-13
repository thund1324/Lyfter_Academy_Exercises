first_list = [1, 2, 3, -58, 0, 8, 16, 181, 42, 7]

for i in range(len(first_list)):
    print(first_list[i])
    if first_list[i] < 0:
        print("Se a encontrado un numero negativo o cero en la lista")
        break