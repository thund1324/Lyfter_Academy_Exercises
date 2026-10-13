def main():
    read_txt()
    lines = organize_txt()
    create_txt(lines)


def read_txt():
    print("-----LISTA ORIGINAL-----")
    with open('songs.txt', 'r', encoding = 'utf-8') as file:
        content = file.read()
        print(content)


def organize_txt():
    lines = []
    with open('songs.txt', 'r', encoding = 'utf-8') as file:
        for line in file:
            lines.append(line.strip())

    lines.sort()
    return lines


def create_txt(lines):
    with open('organize_songs.txt', 'w', encoding = 'utf-8') as file:
        for line in lines:
            file.write(line + "\n")

    print("-----LISTA ORGANIZADA-----")
    with open('organize_songs.txt', 'r', encoding = 'utf-8') as file:
        content = file.read()
        print(content)

main()