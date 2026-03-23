# bases1/polar-bear.py
"""
PolarBear creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=polar-bear
"""
from creature_base import GlobalCreatureBaseClass


class PolarBear(GlobalCreatureBaseClass):
    """
    PolarBear creature
    Size: Large, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 42,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "beast, unaligned",
        "hit_points_up": [4, 4, 4],
        "STR_up": [1, 0, 0],
        "DEX_up": [1, 0, 0],
        "CON_up": [0, 1, 0],
        "INT_up": [0, 1, 0],
        "WIS_up": [0, 0, 1],
        "CHAR_up": [0, 0, 1],
        "abilities": [],
    }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.abilities.extend(['keen_smell'])

    def keen_smell(self) -> str:
        """Keen Smell: The bear has advantage on Wisdom (Perception) checks that rely on smell.ActionsMultiattack. The bear..."""
        return "The bear has advantage on Wisdom (Perception) checks that rely on smell.ActionsMultiattack. The bear makes two attacks: one with its bite and one with its claws.Bite. Melee Weapon Attack: +7 to hit, r"
    def keen_smell(self) -> str:
        """Keen Smell: The bear has advantage on Wisdom (Perception) checks that rely on smell.ActionsMultiattack. The bear..."""
        return "The bear has advantage on Wisdom (Perception) checks that rely on smell.ActionsMultiattack. The bear makes two attacks: one with its bite and one with its claws.Bite. Melee Weapon Attack: +7 to hit, r"

