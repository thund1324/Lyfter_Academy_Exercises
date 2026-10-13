def convert_element(element):
    try:
        return int(element), None
    except ValueError as error:
        return None, f"No se pudo convertir '{element}': {error}"


def process_list(list):
    results = []
    errors = []

    for slot in list:
        number, error = convert_element(slot)
        if error:
            errors.append(error)
        else:
            results.append(number)

    return results, errors



input_list = []

for x in range(5):
    print("-----CONVERTIDOR A ENTERO-----")
    value = input("Ingrese un número: ")
    input_list.append(value)

converted, errors = process_list(input_list)

print("\n-----RESULTADOS-----")
for n in converted:
    print(f"Convertido correctamente: {n}")

print("\n-----ERRORES-----")
for error in errors:
    print(error)

