def search_caracter (word, caracter):
    repaet = 0

    for letter in word:
        if letter == caracter:
            repaet += 1

    print(f"Se repite {caracter} en {word} esta cantidad de veces: {repaet}")


word = input("Ingrese una palabra: ")
caracter = input("Que caracter desea buscar?: ")
print("-----------------------")
search_caracter(word, caracter)