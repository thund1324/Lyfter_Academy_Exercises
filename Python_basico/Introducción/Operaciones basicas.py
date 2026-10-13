print("Selecciona una opción:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
option = input("Ingresa el número de la operación que deseas realizar: ")
num1 =  int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

if option == "1":
    result = num1 + num2
    print("Suma es igual a: ", result)
elif option == "2":
    result = num1 - num2
    print("Resta es igual a: ", result)
elif option == "3":
    result = num1 * num2
    print("Multiplicación es igual a: ", result)
elif option == "4":   
        result = num1 / num2
        print("División es igual a: ", result)
else:
     print("Opción no válida")