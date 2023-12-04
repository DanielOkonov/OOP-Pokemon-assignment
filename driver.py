import argparse
import asyncio
from pokeretriever import PokeRetriever

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
    pokedex_facade = PokeRetriever()

    if args.mode == 'pokemon':
        if args.inputfile:
            with open(args.inputfile, 'r') as file:
                pokemon_names = file.read().splitlines()
                for name in pokemon_names:
                    pokemon = await pokedex_facade.fetch_pokemon_data(name)
                    if pokemon:
                        pokemon_info = str(pokemon)
                        print(pokemon_info)
                        if args.output:
                            with open(args.output, 'a') as f:
                                f.write(pokemon_info + "\n")

    elif args.mode == 'ability':
        if args.inputfile:
            with open(args.inputfile, 'r') as file:
                ability_names = file.read().splitlines()
                for name in ability_names:
                    ability = await pokedex_facade.fetch_ability_data(name)
                    if ability:
                        print(ability)
                        if args.output:
                            with open(args.output, 'a') as f:
                                f.write(str(ability) + "\n")

    elif args.mode == 'move':
        if args.inputfile:
            with open(args.inputfile, 'r') as file:
                move_names = file.read().splitlines()
                for name in move_names:
                    move = await pokedex_facade.fetch_move_data(name)
                    if move:
                        print(move)
                        if args.output:
                            with open(args.output, 'a') as f:
                                f.write(str(move) + "\n")

if __name__ == "__main__":
    asyncio.run(main())
