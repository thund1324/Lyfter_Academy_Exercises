def ask_name():
    name = input("Ingrese su nombre: ")
    if name.isdigit():
        raise ValueError("El nombre no puede ser un número")
    return name


def ask_age():
    try:
        age = int(input("Ingrese su edad: "))
        return age
    except ValueError as error:
        print(f"Edad no valida: {error}")
        return None


def result(name, age):
    if age is not None:
        print(f"Hola, mi nombre es {name} y tengo {age} años")


def main():
    try:
        name = ask_name()
        age = ask_age()
        result(name, age)
    except ValueError as error:
        print(error)


main()
