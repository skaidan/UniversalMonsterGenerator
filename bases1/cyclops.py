# bases1/cyclops.py
"""
Cyclops creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cyclops
"""
from creature_base import GlobalCreatureBaseClass


class Cyclops(GlobalCreatureBaseClass):
    """
    Cyclops creature
    Size: Huge, Type: giant, chaotic neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 138,
        "min_level": 7,
        "level": 7,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "giant, chaotic neutral",
        "hit_points_up": [13, 13, 13],
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
        self.abilities.extend(['poor_depth_perception'])

    def poor_depth_perception(self) -> str:
        """Poor Depth Perception: The cyclops has disadvantage on any attack roll against a target more than 30 feet away.ActionsMulti..."""
        return "The cyclops has disadvantage on any attack roll against a target more than 30 feet away.ActionsMultiattack. The cyclops makes two greatclub attacks.Greatclub. Melee Weapon Attack: +9 to hit, reach 10 "
    def poor_depth_perception(self) -> str:
        """Poor Depth Perception: The cyclops has disadvantage on any attack roll against a target more than 30 feet away.ActionsMulti..."""
        return "The cyclops has disadvantage on any attack roll against a target more than 30 feet away.ActionsMultiattack. The cyclops makes two greatclub attacks.Greatclub. Melee Weapon Attack: +9 to hit, reach 10 "

