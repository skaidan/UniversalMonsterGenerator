# bases1/wraith.py
"""
Wraith creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=wraith
"""
from creature_base import GlobalCreatureBaseClass


class Wraith(GlobalCreatureBaseClass):
    """
    Wraith creature
    Size: Medium, Type: undead, neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 67,
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
        "type": "undead, neutral evil",
        "hit_points_up": [6, 6, 6],
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
        self.abilities.extend(['incorporeal_movement'])

    def incorporeal_movement(self) -> str:
        """Incorporeal Movement: The wraith can move through other creatures and objects as if they were difficult terrain. It takes ..."""
        return "The wraith can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.Sunlight Sensitivity. While in sunlight, "
    def incorporeal_movement(self) -> str:
        """Incorporeal Movement: The wraith can move through other creatures and objects as if they were difficult terrain. It takes ..."""
        return "The wraith can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.Sunlight Sensitivity. While in sunlight, "

