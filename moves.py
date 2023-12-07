class Move:
    """
    The Move class represents a move (or attack) in the Pokémon world.
    It includes details such as the move's name, ID, generation, accuracy, power points (PP),
    power, type, damage class, effect, and the level at which a Pokémon acquires it.
    """

    def __init__(self, name, move_id, generation, accuracy, pp, power, move_type, damage_class, effect_short, level_acquired=None):
        """
        Constructor for the Move class. Initializes a Move object with its details.

        :param name: The name of the move.
        :param move_id: The unique identifier for the move.
        :param generation: The generation of the Pokémon games this move belongs to.
        :param accuracy: The accuracy percentage of the move.
        :param pp: The number of Power Points (PP) of the move.
        :param power: The power score of the move.
        :param move_type: The type of the move (e.g., fire, water).
        :param damage_class: The category of damage caused by the move.
        :param effect_short: A short description of the move's effect.
        :param level_acquired: The level at which a Pokémon can acquire this move, if applicable.
        """
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
        """
        String representation of the Move object. Provides a formatted string with the move's details.

        :return: A string representing the move's details.
        """
        return (f"Name: {self.name}, ID: {self.move_id}, Generation: {self.generation}, "
                f"Accuracy: {self.accuracy}, PP: {self.pp}, Power: {self.power}, "
                f"Type: {self.move_type}, Damage Class: {self.damage_class}, Effect: {self.effect_short}, "
                f"Level Acquired: {self.level_acquired if self.level_acquired is not None else 'N/A'}")
