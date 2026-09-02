flag = False

while flag != True:
    number = int(input("Ingrese del 1 al 10 número: "))
    print("------------------------------")
    if number < 1 or number > 10:
        print("Número no válido. Ingrese un número del 1 al 10.")
    else:
        for i in range(1, 13):
            multiplication = number * i
            print(f"{number} x {i} = {multiplication}")
        flag = True
