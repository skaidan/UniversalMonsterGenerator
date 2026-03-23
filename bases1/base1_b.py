# bases1/base1_b.py
from creature_base import GlobalCreatureBaseClass


class Base1B(GlobalCreatureBaseClass):
    # Valores por defecto de stats para esta clase base
    DEFAULT_STATS = {
        "hit_points": 25,
        "min_level": 4,
        "level": 5,
        "STR": 16,
        "DEX": 14,
        "CON": 14,
        "INT": 11,
        "WIS": 10,
        "CHAR": 9,
        "armor_class": 14,
        "alignment": "Lawful Good",
        "legendary": True,
        "size": "Large",
        "type": "Beast",
        "hit_points_up": [2, 1, 2],
        "STR_up": [1, 0, 1],
        "DEX_up": [0, 1, 0],
        "CON_up": [0, 0, 1],
        "INT_up": [1, 0, 0],
        "WIS_up": [0, 1, 0],
        "CHAR_up": [0, 0, 0],
        "abilities": [],
    }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.abilities.append("Invisibility")

    def method1b(self) -> None:
        print("Base1B method1b")
