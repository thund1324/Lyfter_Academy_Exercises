def main():
    one_line = read_and_clean_txt('saludos.txt')
    one_text = put_together(one_line)
    create_txt(one_text)   

def read_and_clean_txt(entry):
    one_line = []
    print("-----TEXTO ORIGINAL-----")
    with open(entry, 'r', encoding='utf-8') as file:
        content = file.readlines()  
        print("".join(content))

        for line in content:
            one_line.append(line.strip())

    return one_line

def put_together(one_list):
    return " ".join(one_list)

def create_txt(content):

    with open('line.txt', 'w', encoding='utf-8') as file:
        file.write(content)

    print("-----NUEVO TEXTO-----")
    with open('line.txt', 'r', encoding='utf-8') as file:
        print(file.read())

main()

