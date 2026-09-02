info = ["Name", "Age", "State"]
person = ["Gilberto", 25, "Florida"]

person_information = dict(zip(info, person))

print(person_information)
print("--------Información de la persona--------")
print(f"Nombre: {person_information['Name']}")
print(f"Edad: {person_information['Age']}")
print(f"Ciudad: {person_information['State']}")