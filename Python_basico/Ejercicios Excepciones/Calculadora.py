def main(option, result):
    
    if option == 1:
        return addition(result)
    elif option == 2:
        return subtraction(result)
    elif option == 3:
        return multiply(result)
    elif option == 4:
        return split(result)
    elif option == 5:
        return erase_result(result)
    elif option == 6:
        return "exit"
    else:
        print("--------ERROR DETECTADO--------")
        print("Opcion no valida!")
        return result


def addition(result):
    try:
        num = int(input("Ingrese un numero a sumar: "))
        return result + num
    except ValueError  as error:
        print(f"Se ha ingresado un valor equivocado: {error}")
        return result


def subtraction(result):
    try:
        num = int(input("Ingrese un numero a restar: "))
        return result - num
    except ValueError  as error:
        print(f"Se ha ingresado un valor equivocado: {error}")
        return result


def multiply(result):
    try:
        num = int(input("Ingrese un numero a multiplicar: "))
        return result * num
    except ValueError  as error:
        print(f"Se ha ingresado un valor equivocado: {error}")
        return result


def split(result):
    try:
        num = int(input("Ingrese un numero a dividir: "))
        return result / num
    except ZeroDivisionError as error:
        print(f"Operación invalida! No se puede dividir entre cero: {error}")
        return result
    except ValueError  as error:
        print(f"Se ha ingresado un valor equivocado: {error}")
        return result


def erase_result(result):
    result = 0
    return result


result = 0
flag = False
while not flag:
    print("-----CALCULADORA BÁSICA-----")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Borrar resultado actual")
    print("6. Salir")
    print(f"Valor Actua: {result}")
    try:
        option = int(input("Ingrese una opción: "))
        total = main(option, result)
        
        if total == "exit":
            flag = True
        else:
            result = total
    except ValueError as error:
        print("--------ERROR DETECTADO--------")
        print(f"Se ha ingresado un valor equivocado: {error}")
        result = result


print("-----RESULTADO FINAL-----")
print(f"Total : {result}")