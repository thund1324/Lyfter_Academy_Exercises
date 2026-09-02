import csv

def main():
    video_games = dict_create()
    csv_create(video_games)
    tab_separate(video_games)

def dict_create():
    video_games_list = []
    i = 0
    flag = True
    while flag != False:
        print(f"-----INGRESE DATOS DEL JUEGO {i + 1}-----")
        game = {
            'Nombre': input("Ingrese el nombre del juego: "),
            'Género': input("Ingrese el género del juego: "),
            'Desarrollador': input("Ingrese el desarrollador del juego: "),
            'Clasificación ERSB': input("Ingrese la clasificación ERSB del juego: ")
        }

        video_games_list.append(game)
        i += 1
        response = input("¿Desea ingresar otro juego? (s/n): ").lower()
        
        while response not in ['s', 'n']:
            print("Respuesta inválida. Por favor, ingrese 's' para sí o 'n' para no.")
            response = input("¿Desea ingresar otro juego? (s/n): ").lower()
        
        if response == 'n':
                flag = False
        elif response == 's':
            print("Continuando con la opción de ingresar otro juego.")
        
    return video_games_list

def csv_create(video_games_list):
    all_keys = set()
    for game in video_games_list:
        all_keys.update(game.keys())

    header = list(all_keys)

    with open('video_games.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)

        writer.writeheader()
        writer.writerows(video_games_list)


def tab_separate(video_games_list):
    all_keys = set()
    for game in video_games_list:
        all_keys.update(game.keys())

    header = list(all_keys)
    
    with open('video_games_tab.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter='\t')

        writer.writerow(header)

        for game in video_games_list:
            writer.writerow(game.values())


main()