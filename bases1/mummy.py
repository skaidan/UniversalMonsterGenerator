# bases1/mummy.py
"""
Mummy creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mummy
"""
from creature_base import GlobalCreatureBaseClass


class Mummy(GlobalCreatureBaseClass):
    """
    Mummy creature
    Size: Medium, Type: undead, lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 58,
        "min_level": 4,
        "level": 4,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 11,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "undead, lawful evil",
        "hit_points_up": [5, 5, 5],
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
        """Multiattack: The mummy can use its Dreadful Glare and makes one attack with its rotting fist.Rotting Fist. Melee ..."""
        return "The mummy can use its Dreadful Glare and makes one attack with its rotting fist.Rotting Fist. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage plus 10 (3d6"
    def multiattack(self) -> str:
        """Multiattack: The mummy can use its Dreadful Glare and makes one attack with its rotting fist.Rotting Fist. Melee ..."""
        return "The mummy can use its Dreadful Glare and makes one attack with its rotting fist.Rotting Fist. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) bludgeoning damage plus 10 (3d6"

