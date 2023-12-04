import aiohttp

async def fetch_pokemon_data(name_or_id):
    async with aiohttp.ClientSession() as session:
        url = f'https://pokeapi.co/api/v2/pokemon/{name_or_id}'
        async with session.get(url) as response:
            return await response.json()

async def fetch_ability_data(name_or_id):
    async with aiohttp.ClientSession() as session:
        url = f'https://pokeapi.co/api/v2/ability/{name_or_id}'
        async with session.get(url) as response:
            return await response.json()

async def fetch_move_data(name_or_id):
    async with aiohttp.ClientSession() as session:
        url = f'https://pokeapi.co/api/v2/move/{name_or_id}'
        async with session.get(url) as response:
            return await response.json()
