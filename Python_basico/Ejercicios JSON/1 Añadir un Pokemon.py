import json

def main():
    read_json('Pokemon_data.json')
    pokemon = add_pokemon()
    write_json('Pokemon_data.json', pokemon)
    read_json('Pokemon_data.json')


def read_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        pokemons = json.dumps(data, indent=4)
        print(pokemons)


def add_pokemon():
    new_pokemon = {}

    new_pokemon['name'] = input("Ingrese el nombre del nuevo Pokémon: ")
    new_pokemon['Type'] = []
    first_type = input("Ingrese el primer tipo del nuevo Pokémon: ")
    new_pokemon['Type'].append(first_type)
    have_second_type = input("tiene un segundo tipo? (s/n): ").lower()
    if have_second_type == 's':
        second_type = input("Ingrese el segundo tipo del nuevo Pokémon: ")
        new_pokemon['Type'].append(second_type)

    new_pokemon['base_stats'] = {}
    new_pokemon['base_stats']['HP'] = int(input("Ingrese los puntos de vida (HP): "))
    new_pokemon['base_stats']['Attack'] = int(input("Ingrese el valor de ataque: "))
    new_pokemon['base_stats']['Defense'] = int(input("Ingrese el valor de defensa: "))
    new_pokemon['base_stats']['Special Attack'] = int(input("Ingrese el valor de ataque especial: "))
    new_pokemon['base_stats']['Special Defense'] = int(input("Ingrese el valor de defensa especial: "))
    new_pokemon['base_stats']['Speed'] = int(input("Ingrese el valor de velocidad: "))

    return new_pokemon


def write_json(path, new_pokemon):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    data.append(new_pokemon)

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


main()