flag = False

while flag != True:
    number = int(input("Ingresea ingrese un numero entre el 1 y 10: "))
    secret_number = 7

    if number > 0 and number < 11:
        if number == secret_number:
            print("¡Felicidades! Has adivinado el número secreto.")
            flag = True
        else:
            print(f"El número ingresado es: {number}")
            print("Inténtalo de nuevo.")
            print("--------------------------------------------------")
    else:
        print("Por favor, ingrese un número entre el 1 y 10.")
        print("--------------------------------------------------")