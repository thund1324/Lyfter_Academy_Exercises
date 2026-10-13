import json

def main():
    search_type = input("Ingrese el tipo de Pokémon que desea buscar: ")
    filtered_pokemons = search_pokemon_by_type('Pokemon_data.json', search_type)
    read_pokemon_data(filtered_pokemons)

def search_pokemon_by_type(path, search_type):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        filtered_types = []
        for pokemon in data:
            type_pokemon = pokemon['Type']
            search_minus = search_type.lower()

            if isinstance(type_pokemon, str):
                type_pokemon_lower = type_pokemon.lower()
                if search_minus == type_pokemon_lower:
                    filtered_types.append(pokemon)
            elif isinstance(type_pokemon, list):
                minus_types = []
                for type_ in type_pokemon:
                    minus_types.append(type_.lower())

                if search_minus in minus_types:
                    filtered_types.append(pokemon)

    return filtered_types

def read_pokemon_data(pokemons):
    i = 0
    for pokemon in pokemons:
        print("-" * 10, f"POKEMON {i + 1}", "-" * 10)
        print(f"Nombre: {pokemon['name']}")
        print(f"Tipo: {pokemon['Type']}")
        print(f"Nivel: {pokemon['level']}")
        print(f"HP: {pokemon['base_stats']['HP']}")
        print(f"Ataque: {pokemon['base_stats']['Attack']}")
        print(f"Defensa: {pokemon['base_stats']['Defense']}")
        print(f"Ataque especial: {pokemon['base_stats']['Special Attack']}")
        print(f"Defensa especial: {pokemon['base_stats']['Special Defense']}")
        print(f"Velocidad: {pokemon['base_stats']['Speed']}")
        print("-" * 30)
        i += 1

main()