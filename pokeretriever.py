import aiohttp

async def fetch_pokemon_data(pokemon_name_or_id):
    async with aiohttp.ClientSession() as session:
        # Make an API call to fetch Pokemon data
        pass
