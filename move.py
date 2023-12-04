class Move:
    def __init__(self, name, move_id, generation, accuracy, pp, power, type, damage_class, effect):
        self.name = name
        self.move_id = move_id
        self.generation = generation
        self.accuracy = accuracy
        self.pp = pp
        self.power = power
        self.type = type
        self.damage_class = damage_class
        self.effect = effect

    # Additional methods to process or display move data
