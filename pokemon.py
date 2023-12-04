class Pokemon:
    def __init__(self, name, pokemon_id, height, weight, stats, types, abilities, moves):
        self.name = name
        self.pokemon_id = pokemon_id
        self.height = height
        self.weight = weight
        self.stats = stats  # List of PokemonStat objects
        self.types = types  # List of type names (strings)
        self.abilities = abilities  # List of Ability objects
        self.moves = moves  # List of Move objects

    def __str__(self):
        types_str = ', '.join(self.types)
        stats_str = "\n".join([f"('{stat.name}', {stat.base_stat})" for stat in self.stats])
        abilities_str = "\n".join([ability.name for ability in self.abilities])
        moves_str = "\n".join(
            [f"('Move name: {move.name}', 'Level acquired: {move.level_acquired}')" for move in self.moves])

        return (f"Name: {self.name}\n"
                f"ID: {self.pokemon_id}\n"
                f"Height: {self.height}\n"
                f"Weight: {self.weight}\n"
                f"Types: {types_str}\n\n"
                f"Stats:\n------\n{stats_str}\n"
                f"Abilities:\n------\n{abilities_str}\n"
                f"Moves:\n-------\n{moves_str}")