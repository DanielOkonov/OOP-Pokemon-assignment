class Ability:
    def __init__(self, name, ability_id, generation, effect, effect_short, pokemon):
        self.name = name
        self.ability_id = ability_id
        self.generation = generation
        self.effect = effect
        self.effect_short = effect_short
        self.pokemon = pokemon  # List of Pokémon that can have this ability

    # Additional methods for ability-related processing
