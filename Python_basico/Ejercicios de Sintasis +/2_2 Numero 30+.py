for i in range(0, 3):
    number = int(input("Ingrese un número: "))
    
    if i == 0:
        number1 = number
    elif i == 1:
        number2 = number
    else:
        number3 = number

total = number1 + number2 + number3

if number1 == 30 or number2 == 30 or number3 == 30:
    print("¡Correcto!")
elif total == 30:
    print("¡Correcto!")
else:
    print("Incorrecto. Ninguno de los números es 30 y la suma no es 30.")