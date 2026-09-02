import csv

def main():
    games = read_games('video_games.csv')
    search_esrb = input("Ingrese la clasificación ERSB que desea mostrar: ")
    filtered_games = filter_esrb(games, search_esrb)
    print_filtered_games(filtered_games)


def read_games(path):
    list_games = []
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            list_games.append(row)
    return list_games


def filter_esrb(games, esrb):
    filtered = []
    for game in games:
        if game['Clasificación ERSB'].lower() == esrb.lower():
            filtered.append(game)
    return filtered


def print_filtered_games(filtered_games):
    if not filtered_games:
        print("No se encontraron juegos con la clasificación ERSB especificada.")
    else:
        for i, game in enumerate(filtered_games):
            print(f"------DATOS DEL JUEGO NUMERO {i + 1}------")
            print(f"Nombre: {game['Nombre']}")
            print(f"Género: {game['Género']}")
            print(f"Desarrollador: {game['Desarrollador']}")
            print(f"Clasificación ERSB: {game['Clasificación ERSB']}")


main()