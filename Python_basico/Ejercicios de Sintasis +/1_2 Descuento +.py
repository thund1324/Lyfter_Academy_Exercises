flag = False

while flag != True:
    product = float(input("Ingrese el precio del producto: "))

    if product < 100 and product > 0:
        discount = product * 0.02
        print(f"Descuento del 2%: {discount}")
        flag = True
    elif product >= 100:
        discount = product * 0.10
        print(f"Descuento del 10%: {discount}")
        flag = True
    else:
        print("Precio no válido, ingrese un precio valido.")
        print("-----------------------------------------")
    

print("--------------TOTAL A PAGAR--------------")

apply_discount = product - discount

print(f"Total a pagar: {apply_discount}")