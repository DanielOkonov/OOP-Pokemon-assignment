class Stat:
    def __init__(self, name, stat_id, is_battle_only, base_stat):
        self.name = name
        self.stat_id = stat_id
        self.is_battle_only = is_battle_only
        self.base_stat = base_stat

    def __str__(self):
        return f"Name: {self.name}, ID: {self.stat_id}, Is Battle Only: {self.is_battle_only}, Base Stat: {self.base_stat}"
