class Ability:
    def __init__(self, name, ability_id, generation, effect, effect_short, pokemon):
        self.name = name
        self.ability_id = ability_id
        self.generation = generation
        self.effect = effect
        self.effect_short = effect_short
        self.pokemon = pokemon  # List of Pokémon names

    def __str__(self):
        return f"Name: {self.name}, ID: {self.ability_id}, Generation: {self.generation}, Effect: {self.effect}, Effect (Short): {self.effect_short}, Pokemon: {', '.join(self.pokemon)}"
