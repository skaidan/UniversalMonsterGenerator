# bases1/base1_a.py
from creature_base import GlobalCreatureBaseClass


class Base1A(GlobalCreatureBaseClass):
    # Valores por defecto de stats para esta clase base
    DEFAULT_STATS = {
        "hit_points": 20,
        "min_level": 3,
        "level": 3,
        "STR": 14,
        "DEX": 12,
        "CON": 16,
        "INT": 10,
        "WIS": 11,
        "CHAR": 8,
        "armor_class": 15,
        "alignment": "Chaotic Evil",
        "legendary": False,
        "size": "Medium",
        "type": "Humanoid",
        "hit_points_up": [1, 2, 1],
        "STR_up": [1, 1, 0],
        "DEX_up": [0, 0, 0],
        "CON_up": [1, 0, 1],
        "INT_up": [0, 0, 1],
        "WIS_up": [0, 1, 0],
        "CHAR_up": [0, 0, 0],
        "abilities": [],
    }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.abilities.append("ThiefTraining")

    def method1(self) -> None:
        print("Base1A.method1")
