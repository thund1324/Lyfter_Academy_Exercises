def main():
    content = read_txt('saludos.txt')
    count_words(content)


def read_txt(entry):
    print("-----TEXTO ORIGINAL-----")
    with open(entry, 'r', encoding='utf-8') as file:
        content = file.read()  
        print(content)
    return content


def count_words(content):
    words = content.split()
    total = len(words)        
    
    print("-----RESULTADO-----")
    print(f"Este archivo contiene {total} palabras")


main()
