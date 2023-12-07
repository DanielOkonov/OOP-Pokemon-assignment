import aiohttp
from moves import Move
from statistics import Stat
from ability import Ability
from pokemon import Pokemon

class PokeRetriever:
    """
    The PokeRetriever class is responsible for retrieving data from the PokeAPI.
    It fetches data about Pokemon, including their moves, abilities, and statistics.
    """

    def __init__(self):
        """
        Constructor for the PokeRetriever class. Initializes the base URL for the PokeAPI.
        """
        self.base_url = "https://pokeapi.co/api/v2"

    async def fetch_pokemon_data(self, pokemon_name_or_id):
        """
        Asynchronously fetches data for a specific Pokemon by name or ID.

        :param pokemon_name_or_id: The name or ID of the Pokemon.
        :return: A Pokemon object with fetched data, or None if the request fails.
        """
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}/pokemon/{pokemon_name_or_id}"
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()

                    # Parsing Stats
                    stats = [Stat(
                        name=s['stat']['name'],
                        stat_id=int(s['stat']['url'].split('/')[-2]),
                        is_battle_only=False,
                        base_stat=s['base_stat']
                    ) for s in data['stats']]

                    # Parsing Moves
                    moves = []
                    for m in data['moves']:
                        move_data = await self.fetch_move_data(m['move']['name'])
                        if move_data:
                            moves.append(move_data)

                    # Parsing Abilities
                    abilities = []
                    for a in data['abilities']:
                        ability_data = await self.fetch_ability_data(a['ability']['name'])
                        if ability_data:
                            abilities.append(ability_data)

                    # Creating Pokemon object
                    pokemon = Pokemon(
                        name=data['name'],
                        pokemon_id=data['id'],
                        height=data['height'],
                        weight=data['weight'],
                        stats=stats,
                        types=[t['type']['name'] for t in data['types']],
                        abilities=abilities,
                        moves=moves
                    )

                    return pokemon
                else:
                    return None

    async def fetch_move_data(self, move_name_or_id):
        """
        Asynchronously fetches data for a specific move by name or ID.

        :param move_name_or_id: The name or ID of the move.
        :return: A Move object with fetched data, or None if the request fails.
        """
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}/move/{move_name_or_id}"
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    effect_short = data['effect_entries'][0]['short_effect'] if data[
                        'effect_entries'] else "No effect description"
                    move = Move(
                        name=data['name'],
                        move_id=data['id'],
                        generation=data['generation']['name'],
                        accuracy=data['accuracy'],
                        pp=data['pp'],
                        power=data['power'],
                        move_type=data['type']['name'],
                        damage_class=data['damage_class']['name'],
                        effect_short=effect_short
                    )
                    return move
                else:
                    return None

    async def fetch_ability_data(self, ability_name_or_id):
        """
        Asynchronously fetches data for a specific ability by name or ID.

        :param ability_name_or_id: The name or ID of the ability.
        :return: An Ability object with fetched data, or None if the request fails.
        """
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}/ability/{ability_name_or_id}"
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()

                    # Extract necessary data to instantiate an Ability object
                    pokemon_list = [p['pokemon']['name'] for p in data['pokemon']]
                    ability = Ability(
                        name=data['name'],
                        ability_id=data['id'],
                        generation=data['generation']['name'],
                        effect=data['effect_entries'][0]['effect'],
                        effect_short=data['effect_entries'][0]['short_effect'],
                        pokemon=pokemon_list
                    )
                    return ability
                else:
                    return None


