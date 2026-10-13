first_list = [1, 2, 3, -58, 0, 8, 16, 181, 42, 7]

all_positive = True         

for i in range(len(first_list)):
    print(first_list[i])
    if first_list[i] <= 0:
        all_positive = False    

print("Resultado final:")

if all_positive == True:
    print("Todos los números son positivos.")
else:
    print("Se ha encontrado un número negativo o cero en la lista.")