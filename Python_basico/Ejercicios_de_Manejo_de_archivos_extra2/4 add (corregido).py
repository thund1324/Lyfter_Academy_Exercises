def main():
    read_txt()
    insert_text()


def read_txt():
    print("-----TEXTO ORIGINAL-----")
    with open('saludos.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()  
        print("".join(content))


def insert_text():
    print("-----NUEVA LINEA-----")
    add = input("Añada un nueva linea: ")
    
    with open('saludos.txt', 'a', encoding = 'utf-8') as file:
        file.write('\n' + add)
    
    print("-----RESULTADO-----")
    with open('saludos.txt', 'r', encoding='utf-8') as file:
        print(file.read())


main()