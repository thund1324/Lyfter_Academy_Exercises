flag = False

while flag != True:
    seconds = int(input("Ingrese los segundos: "))

    if seconds < 600 and seconds >= 0:
        print("cantidad de segundos es menor a 10 minutos")
        print(f"Cantidad de segundos faltantes para llegar a 10 minutos: {600 - seconds}")
        flag = True
    elif seconds == 600:
        print("Cantidad de segundos es igual a 10 minutos")
        flag = True
    elif seconds > 600:
        print("Cantidad de segundos es mayor a 10 minutos")
        print(f"Cantidad de segundos excedentes: {seconds - 600}")
        flag = True
    else:
        print("Ingrese un valor válido")
        print("-----------------------------------------")
