def first_function(word):
    count_upper = 0
    count_lower = 0
    for caracter in word:
        if caracter.isupper():
            count_upper += 1
        elif caracter.islower():
            count_lower += 1
    
    print(f"Minusculas: {count_lower} || Mayusculas: {count_upper}")


word = input("Ingrese una palabra o frase: ")
print("--------------------------")
first_function(word)