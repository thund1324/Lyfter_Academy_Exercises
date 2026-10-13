import csv

def main():
    read_line_by_line('video_games.csv')

def read_line_by_line(path):
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        i = 0
        for row in reader:
            print(f"------DATOS DEL JUEGO NUMERO {i + 1}------")
            print(f"Nombre: {row['Nombre']}")
            print(f"Género: {row['Género']}")
            print(f"Desarrollador: {row['Desarrollador']}")
            print(f"Clasificación ERSB: {row['Clasificación ERSB']}")
            i += 1

main()