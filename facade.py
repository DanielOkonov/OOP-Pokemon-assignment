import aiohttp


class PokeRetriever:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2"

    async def fetch_pokemon_data(self, pokemon_name_or_id):
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}/pokemon/{pokemon_name_or_id}"
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None  # Or handle error appropriately

    async def fetch_ability_data(self, ability_name_or_id):
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}/ability/{ability_name_or_id}"
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None  # Or handle error appropriately

    async def fetch_move_data(self, move_name_or_id):
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}/move/{move_name_or_id}"
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return None  # Or handle error appropriately
