class Ability:
    """
    The Ability class represents an ability in the Pokémon world.
    It encapsulates details such as the ability name, ID, the generation it belongs to,
    its effects, and the Pokémon that can have this ability.
    """

    def __init__(self, name, ability_id, generation, effect, effect_short, pokemon):
        """
        Constructor for the Ability class. Initializes an Ability object with its details.

        :param name: The name of the ability.
        :param ability_id: The unique identifier for the ability.
        :param generation: The generation of the Pokémon games this ability belongs to.
        :param effect: The detailed description of the ability's effect.
        :param effect_short: A short description of the ability's effect.
        :param pokemon: A list of Pokémon names that can have this ability.
        """
        self.name = name
        self.ability_id = ability_id
        self.generation = generation
        self.effect = effect
        self.effect_short = effect_short
        self.pokemon = pokemon  # List of Pokémon names

    def __str__(self):
        """
        String representation of the Ability object. Provides a formatted string
        with the ability's details.

        :return: A string representing the ability's details.
        """
        return f"Name: {self.name}, ID: {self.ability_id}, Generation: {self.generation}, Effect: {self.effect}, Effect (Short): {self.effect_short}, Pokemon: {', '.join(self.pokemon)}"
