def first_function(word):
    reverse = ""
    for caracter in range(len(word) -1, -1, -1):
        reverse += word[caracter]
    return reverse


word = "Hello word - drow olleH"
print(first_function(word))