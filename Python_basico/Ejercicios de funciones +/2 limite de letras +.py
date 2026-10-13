def caracter_number(words, letter_limit):
    limit_words = []
    for word in words:
        if len(word) > letter_limit:
            limit_words.append(word)
    return limit_words

words = ["Murcielago", "Pikachu", "Mago"        , "Esternocleidomastoideo", "Perro", "Gato", "Pupusa"]      
letter_limit = int(input("Ingrese la cantidad minima de letras: "))
print("----------MOSTRANDO RESULTADO----------")

result = caracter_number(words, letter_limit)
print(result)