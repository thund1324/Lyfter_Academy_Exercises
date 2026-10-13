import json

def main():
    pokemon_list = list_maker('Pokemon_data.json')
    show_stats(pokemon_list)


def list_maker(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        pokemons = []

        for pokemon in data:
            pokemons.append(pokemon)

    return pokemons

def show_stats(pokemon_list):
    i = 0
    for pokemon in pokemon_list:
        print("-" * 10, f"POKEMON {i + 1}", "-" * 10)
        print(f"Nombre: {pokemon['name']}")
        print(f"Ataque: {pokemon['base_stats']['Attack']}")
        print(f"Defensa: {pokemon['base_stats']['Defense']}")
        print(f"Velocidad: {pokemon['base_stats']['Speed']}")
        print("-" * 31)
        i += 1

main()