import aiohttp


class PokeRetriever:
    """
    The PokeRetriever class provides a simplified interface to the PokeAPI.
    It fetches basic data about Pokemon, their abilities, and moves.
    """

    def __init__(self):
        """
        Constructor for the PokeRetriever class. Initializes the base URL for the PokeAPI.
        """
        self.base_url = "https://pokeapi.co/api/v2"

    async def fetch_pokemon_data(self, pokemon_name_or_id):
        """
        Asynchronously fetches basic data for a specific Pokemon by name or ID.

        :param pokemon_name_or_id: The name or ID of the Pokemon.
        :return: JSON data of the Pokemon, or None if the request fails.
        """
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}/pokemon/{pokemon_name_or_id}"
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None  # Or handle error appropriately

    async def fetch_ability_data(self, ability_name_or_id):
        """
        Asynchronously fetches basic data for a specific ability by name or ID.

        :param ability_name_or_id: The name or ID of the ability.
        :return: JSON data of the ability, or None if the request fails.
        """
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}/ability/{ability_name_or_id}"
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None  # Or handle error appropriately

    async def fetch_move_data(self, move_name_or_id):
        """
        Asynchronously fetches basic data for a specific move by name or ID.

        :param move_name_or_id: The name or ID of the move.
        :return: JSON data of the move, or None if the request fails.
        """
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}/move/{move_name_or_id}"
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None  # Or handle error appropriately
