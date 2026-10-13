number = int(input("Ingrese un número: "))
total = 0

for i in range(1, number + 1):
    total += i

print(f"La suma de los números del 1 al {number} es: {total}")
