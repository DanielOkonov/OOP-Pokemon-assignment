class Pokemon:
    """
    The Pokemon class represents a Pokémon, encapsulating various attributes like
    its name, ID, physical traits (height and weight), and its capabilities such as
    stats, types, abilities, and moves.
    """

    def __init__(self, name, pokemon_id, height, weight, stats, types, abilities, moves):
        """
        Constructor for the Pokemon class. Initializes a Pokemon object with its attributes.

        :param name: The name of the Pokémon.
        :param pokemon_id: The unique identifier for the Pokémon.
        :param height: The height of the Pokémon.
        :param weight: The weight of the Pokémon.
        :param stats: A list of Stat objects representing the Pokémon's statistics.
        :param types: A list of type names (strings) representing the Pokémon's types.
        :param abilities: A list of Ability objects representing the abilities of the Pokémon.
        :param moves: A list of Move objects representing the moves the Pokémon can learn.
        """
        self.name = name
        self.pokemon_id = pokemon_id
        self.height = height
        self.weight = weight
        self.stats = stats  # List of PokemonStat objects
        self.types = types  # List of type names (strings)
        self.abilities = abilities  # List of Ability objects
        self.moves = moves  # List of Move objects

    def __str__(self):
        """
        String representation of the Pokemon object. Provides a formatted string with
        the Pokémon's detailed attributes.

        :return: A string representing the Pokémon's attributes.
        """
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