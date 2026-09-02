def main():
    words = read_txt()
    make_upper(words)

def read_txt():
    words = []
    print("-----TEXTO ORIGINAL-----")
    with open('saludos.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()  
        print("".join(content))

        for line in content:
            words.append(line)
    
    return words

def make_upper(words):
    uppers = []
    for word in words:
        uppers.append(word.upper())
    
    with open('mayus.txt', 'w', encoding = 'utf-8') as file:
        for word in uppers:
            file.writelines(word)
    print("-----RESULTADO-----")
    with open('mayus.txt', 'r', encoding = 'utf-8') as file:
        content = file.readlines()
        print("".join(content))


main()