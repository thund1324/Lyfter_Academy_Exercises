string1 = str(input("Ingrese una palabra: "))
string2 = str(input("Ingrese otra palabra: "))

# Noto que aqui no es necesario convertir a string a otro tipo de variable, ya que el input ya devuelve un string
result = string1 + " " + string2

print(f"La concatenación de '{string1}' y '{string2}' es: '{result}'")
print("------------------------------------------------------------------")
print (" ")

string1 = str(input("ingrese una palabra: "))
int1 = int(input("Ingrese un número entero: "))

# En este caso, es necesario convertir el número entero a string para poder concatenarlo con la palabra
# Ya que no se pueden concatenar directamente un string y un entero.
# Si no se realiza la conversión, se generará un error de tipo (TypeError) indicando que no se pueden concatenar tipos diferentes.
result = string1 + " " + str(int1)

print(f"La concatenación de '{string1}' y '{int1}' es: '{result}'")
print("------------------------------------------------------------------")
print (" ")

int1 = int(input("Ingrese un número entero: "))
string1 = str(input("ingrese una palabra: "))

# Al igual que en el caso anterior, es necesario convertir el número entero a string para poder concatenarlo con la palabra.
result = str(int1) + " " + string1

print(f"La concatenación de '{int1}' y '{string1}' es: '{result}'")
print("------------------------------------------------------------------")
print (" ")

list1 = list(input("Ingrese una lista de elementos separados por comas: ").split(","))
list2 = list(input("Ingrese otra lista de elementos separados por comas: ").split(","))

# En este caso, no es necesario convertir las listas a otro tipo de variable, ya que la concatenación de listas
# se realiza mediante el operador +, que une los elementos de ambas listas en una nueva lista.
result = list1 + list2

print(f"La concatenación de '{list1}' y '{list2}' es: '{result}'")
print("------------------------------------------------------------------")
print (" ") 

string1 = str(input("ingrese una palabra: "))
list1 = list(input("Ingrese una lista de elementos separados por comas: ").split(","))

# En este caso, es necesario convertir la lista a string para poder concatenarla con la palabra.
# Si no se realiza la conversión, se generará un error de tipo (TypeError) indicando que no se pueden concatenar tipos diferentes.
result = string1 + " " + str(list1)

print(f"La concatenación de '{string1}' y '{list1}' es: '{result}'")
print("------------------------------------------------------------------")
print (" ")

float1 = float(input("Ingrese un número decimal: "))
int1 = int(input("Ingrese un número entero: "))

# En este caso, no es necesario convertir el número decimal a entero o viceversa, ya que la suma de un número decimal 
# y un número entero se realiza sin necesidad de conversión.
result = float1 + int1

print(f"La suma de '{float1}' y '{int1}' es: '{result}'")
print("------------------------------------------------------------------")
print (" ")

bool1 = bool(input("Ingrese un valor booleano (True/False): "))
bool2 = bool(input("Ingrese otro valor booleano (True/False): "))

# En este caso, no es necesario convertir los valores booleanos a otro tipo de variable, ya que la operación lógica AND 
# Se realiza directamente entre los valores booleanos.
# Y si solo coloco un "+" en vez de "and", se realizará una suma de los valores booleanos
# Donde True se considera como 1 y False como 0.
# Me da una suma, donde si coloco True + True, el resultado será 2, si coloco True + False, el resultado será 1
# Y si coloco False + False, el resultado será 0.
result = bool1 and bool2

print(f"La operación lógica AND entre '{bool1}' y '{bool2}' es: '{result}'")
print("------------------------------------------------------------------")
print ("FIN DEL PROGRAMA")