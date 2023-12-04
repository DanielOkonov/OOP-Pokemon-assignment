class Move:
    def __init__(self, name, move_id, generation, accuracy, pp, power, move_type, damage_class, effect_short, level_acquired=None):
        self.name = name
        self.move_id = move_id
        self.generation = generation
        self.accuracy = accuracy
        self.pp = pp
        self.power = power
        self.move_type = move_type
        self.damage_class = damage_class
        self.effect_short = effect_short
        self.level_acquired = level_acquired  # Optional attribute, defaulting to None

    def __str__(self):
        return (f"Name: {self.name}, ID: {self.move_id}, Generation: {self.generation}, "
                f"Accuracy: {self.accuracy}, PP: {self.pp}, Power: {self.power}, "
                f"Type: {self.move_type}, Damage Class: {self.damage_class}, Effect: {self.effect_short}, "
                f"Level Acquired: {self.level_acquired if self.level_acquired is not None else 'N/A'}")
