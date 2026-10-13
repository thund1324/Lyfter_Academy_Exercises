import csv

def main():
    games = read_games('video_games.csv')
    count = counter_genres(games)
    print_results(count)


def read_games(path):
    list_games = []
    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            list_games.append(row)
    return list_games


def counter_genres(games):
    genres_count = {}
    for game in games:
        genre = game['Género']
        if genre in genres_count:
            genres_count[genre] += 1
        else:
            genres_count[genre] = 1
    return genres_count


def print_results(count):
    print("-----CONTADOR DE GÉNEROS-----")
    for genre, count in count.items():
        print(f"Género: {genre} - Cantidad de juegos: {count}")

main()