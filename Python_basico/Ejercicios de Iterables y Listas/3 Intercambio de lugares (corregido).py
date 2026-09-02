first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Lista original: {first_list}")
change = first_list[0]
first_list[0] = first_list[-1]
first_list[-1] = change

print("Iniciando el intercambio de lugares...")

print(f"Lista después del intercambio: {first_list}")