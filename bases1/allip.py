# bases1/allip.py
"""
Allip creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=allip
"""
from creature_base import GlobalCreatureBaseClass


class Allip(GlobalCreatureBaseClass):
    """
    Allip creature
    Size: Medium, Type: Undead, typically Neutral Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 40,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Undead, typically Neutral Evil",
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
        # Add creature-specific abilities
        self.abilities.extend(['incorporeal_movement'])

    def incorporeal_movement(self) -> str:
        """Incorporeal Movement: The allip can move through other creatures and objects as if they were difficult terrain. It takes 5..."""
        return "The allip can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.Unusual Nature. The allip doesn't require "

