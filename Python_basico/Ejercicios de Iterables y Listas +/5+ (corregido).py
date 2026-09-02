first_list = []
second_list = []
word = ""

while True:
    word = str(input("Ingrese un palabra: "))
    first_list.append(word)
    
    while True:
        option = input("Ingresar otra palabra? (y/n): ")
        if option == "y" or option == "n":
            break
        else:
            print("Opcion no valida, ingrese y o n")
    if option == "n":
        break

for word in first_list:
    if len(word) > 4:
        second_list.append(word)

print(f"Lista de palabras ingresadas: {first_list}")
print(f"Las palabras con más de 4 caracteres son: {second_list}")   