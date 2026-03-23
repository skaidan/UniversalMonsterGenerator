# bases1/wyvern.py
"""
Wyvern creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=wyvern
"""
from creature_base import GlobalCreatureBaseClass


class Wyvern(GlobalCreatureBaseClass):
    """
    Wyvern creature
    Size: Large, Type: dragon, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 110,
        "min_level": 7,
        "level": 7,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "dragon, unaligned",
        "hit_points_up": [11, 11, 11],
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
        self.abilities.extend(['multiattack'])

    def multiattack(self) -> str:
        """Multiattack: The wyvern makes two attacks: one with its bite and one with its stinger. While flying, it can use i..."""
        return "The wyvern makes two attacks: one with its bite and one with its stinger. While flying, it can use its claws in place of one other attack.Bite. Melee Weapon Attack: +7 to hit, reach 10 ft., one creatu"
    def multiattack(self) -> str:
        """Multiattack: The wyvern makes two attacks: one with its bite and one with its stinger. While flying, it can use i..."""
        return "The wyvern makes two attacks: one with its bite and one with its stinger. While flying, it can use its claws in place of one other attack.Bite. Melee Weapon Attack: +7 to hit, reach 10 ft., one creatu"

