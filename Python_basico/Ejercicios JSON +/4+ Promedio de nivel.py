import json

def main():
    filtered_pokemons = dic_maker('Pokemon_data.json')
    prom_level = calculate_average_level(filtered_pokemons)
    print_average_levels(prom_level)

def dic_maker(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        pokemons = {
            'Fire': [],
            'Water': [],
            'Grass': [],
            'Electric': [],
            'Normal': [],
            'Rock': [],
            'Psychic': [],
            'Dragon': [],
            'Fighting': [],
            'Poison': [],
            'Ground': [],
            'Bug': [],
            'Flying': [],
            'Ghost': [],
            'Ice': [],
            'Steel': [],
            'Dark': [],
            'Fairy': []
            }

        for pokemon in data:
            if 'Fire' in pokemon['Type']:
                pokemons['Fire'].append(pokemon['level'])
            if 'Water' in pokemon['Type']:
                pokemons['Water'].append(pokemon['level'])
            if 'Grass' in pokemon['Type']:
                pokemons['Grass'].append(pokemon['level'])
            if 'Electric' in pokemon['Type']:
                pokemons['Electric'].append(pokemon['level'])
            if 'Normal' in pokemon['Type']:
                pokemons['Normal'].append(pokemon['level'])
            if 'Rock' in pokemon['Type']:
                pokemons['Rock'].append(pokemon['level'])
            if 'Psychic' in pokemon['Type']:
                pokemons['Psychic'].append(pokemon['level'])
            if 'Dragon' in pokemon['Type']:
                pokemons['Dragon'].append(pokemon['level'])
            if 'Fighting' in pokemon['Type']:
                pokemons['Fighting'].append(pokemon['level'])
            if 'Poison' in pokemon['Type']:
                pokemons['Poison'].append(pokemon['level'])
            if 'Ground' in pokemon['Type']:
                pokemons['Ground'].append(pokemon['level'])
            if 'Bug' in pokemon['Type']:
                pokemons['Bug'].append(pokemon['level'])
            if 'Flying' in pokemon['Type']:
                pokemons['Flying'].append(pokemon['level'])
            if 'Ghost' in pokemon['Type']:
                pokemons['Ghost'].append(pokemon['level'])
            if 'Ice' in pokemon['Type']:
                pokemons['Ice'].append(pokemon['level'])
            if 'Steel' in pokemon['Type']:
                pokemons['Steel'].append(pokemon['level'])
            if 'Dark' in pokemon['Type']:
                pokemons['Dark'].append(pokemon['level'])
            if 'Fairy' in pokemon['Type']:
                pokemons['Fairy'].append(pokemon['level'])

    return pokemons


def calculate_average_level(pokemons):
    average_levels = {}
    for type_, levels in pokemons.items():
        if levels:
            average_levels[type_] = sum(levels) / len(levels)
        else:
            average_levels[type_] = 0

    return average_levels


def print_average_levels(average_levels):
    print("Promedio de nivel por tipo de Pokémon:")
    for type_, avg_level in average_levels.items():
        print(f"{type_}: {avg_level:.2f}")


main()