fist_name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
age = int(input("Ingrese su edad: "))

if age == 1:
    print("Eres un bebé.")
elif age <= 8:
    print("Eres un niño.")
elif age <= 12:
    print("Eres un preadolescente.")
elif age <= 19:
    print("Eres un adolescente.")
elif age <= 30:
    print("Eres un joven adulto.")
elif age <= 44:
    print("Eres un adulto.")
elif age <= 60:
    print("Eres un adulto mayor.")
elif age > 60:
    print("Eres un anciano.")
else:
    print("Edad no válida.")
print("------------------------------------------------------------------")
