def vowels_number(word):
    vowels = "aeiouAEIOU"
    count = 0

    for letter in word:
        if letter in vowels:
            count += 1

    return count


word = input("Ingrese una palabra: ")
print(vowels_number(word))
