# bases1/specter.py
"""
Specter creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=specter
"""
from creature_base import GlobalCreatureBaseClass


class Specter(GlobalCreatureBaseClass):
    """
    Specter creature
    Size: Medium, Type: undead, chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 22,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "undead, chaotic evil",
        "hit_points_up": [2, 2, 2],
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
        """Incorporeal Movement: The specter can move through other creatures and objects as if they were difficult terrain. It takes..."""
        return "The specter can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.Sunlight Sensitivity. While in sunlight,"
    def incorporeal_movement(self) -> str:
        """Incorporeal Movement: The specter can move through other creatures and objects as if they were difficult terrain. It takes..."""
        return "The specter can move through other creatures and objects as if they were difficult terrain. It takes 5 (1d10) force damage if it ends its turn inside an object.Sunlight Sensitivity. While in sunlight,"

