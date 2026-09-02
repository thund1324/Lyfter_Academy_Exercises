celsius = float(input("Ingrese la temperatura en Celsius: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print("------------------------")
print(f"Temperatura en Fahrenheit: {fahrenheit:.2f} °F")
print(f"Temperatura en Kelvin: {kelvin:.2f} K")