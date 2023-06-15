import requests

from typing import Dict, Optional
import random
import requests
from pokemon import Pokemon, Statistic

POKEMON_ENDPOINT = "https://pokeapi.co/api/v2/pokemon/"

def get_random_pokemon() -> Dict[str, str]:
    pokemon_id = random.randint(1, 1010)
    pokemon = requests.get(f"{POKEMON_ENDPOINT}{pokemon_id}")
    return pokemon.json()
def convert_json_to_pokemon(api_response: Dict[str, str]) -> Pokemon:
    name = api_response["name"]
    response_stats = api_response["stats"]
    stats = []
    for response_stat in response_stats:
        stats.append(Statistic(response_stat["base_stat"],
                               response_stat["stat"]["name"]))
    return Pokemon(name, stats)


def get_all_stats_names():
    names = []
    base_url = "https://pokeapi.co/api/v2/stat/"

    for i in range(1, 10):
        url = f'{base_url}/{i}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            names.append(data['name'])
        else:
            print(f'Error occurred while fetching data for ID {i}')

    return names

def choose_winner(pokemon1: Pokemon, pokemon2: Pokemon) -> Optional[Pokemon]:
    all_stats = 



pokemon_names = get_all_stats_names()
p1_score = 0
p2_score = 0

for statistic in all_stats:
    p1_stat_points = pokemon1.get_statistic
print(pokemon_names)


api_response = get_random_pokemon()
pokemon = convert_json_to_pokemon(api_response)
print(pokemon)





