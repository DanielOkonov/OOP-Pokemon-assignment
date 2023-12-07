class Stat:
    """
    The Stat class represents a statistic (or stat) for a Pokémon.
    It includes details such as the stat's name, ID, whether it is used only in battles, and its base value.
    """

    def __init__(self, name, stat_id, is_battle_only, base_stat):
        """
        Constructor for the Stat class. Initializes a Stat object with its details.

        :param name: The name of the stat.
        :param stat_id: The unique identifier for the stat.
        :param is_battle_only: A boolean indicating if the stat is used only in battles.
        :param base_stat: The base value of the stat.
        """
        self.name = name
        self.stat_id = stat_id
        self.is_battle_only = is_battle_only
        self.base_stat = base_stat

    def __str__(self):
        """
        String representation of the Stat object. Provides a formatted string with the stat's details.

        :return: A string representing the stat's details.
        """
        return f"Name: {self.name}, ID: {self.stat_id}, Is Battle Only: {self.is_battle_only}, Base Stat: {self.base_stat}"
