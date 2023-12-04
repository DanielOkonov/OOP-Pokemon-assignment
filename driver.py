import argparse
import asyncio
from facade import PokedexFacade

def parse_arguments():
    parser = argparse.ArgumentParser(description='Pokédex Application')
    parser.add_argument('mode', choices=['pokemon', 'ability', 'move'], help='Mode of the application')
    parser.add_argument('--inputfile', help='Input file with data')
    parser.add_argument('--inputdata', help='Direct input data')
    parser.add_argument('--expanded', action='store_true', help='Expanded information flag')
    parser.add_argument('--output', help='Output file name')
    return parser.parse_args()

async def main():
    args = parse_arguments()
    pokedex_facade = PokedexFacade()
    result = await pokedex_facade.execute_request(args)
    # Handle and display the result

if __name__ == "__main__":
    asyncio.run(main())
