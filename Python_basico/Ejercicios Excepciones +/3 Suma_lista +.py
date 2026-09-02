def float_converter(num, num_list):
    try:
        num = float(num)
        num_list.append(num)
    except ValueError as error:
        print("-----ERROR DETECTADO-----")
        num_list.append(num)
        print(f"Error debido a: {error}")

def addition_value(num_list, addition_list):
    total = 0
    for number in num_list:
        try:
            total += number
            addition_list.append(f"{number} sumado correctamente")
        except TypeError:
            addition_list.append(f"Elemento invalido: {number}")
    return total    


num_list = []
addition_list = []


for x in range(0, 5):
    print("-----SUMA DE UNA LISTA-----")
    num = input("Ingrese un numero: ")
    float_converter(num, num_list)

    if x == 4:
        total = addition_value(num_list, addition_list)


print("-----RESULTADO-----")
print(f"Elementos sumados: {num_list}")
for slot in addition_list   :
    print(slot)
print(f"Total de la suma: {total:.2f}")