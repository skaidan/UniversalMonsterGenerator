# bases1/banshee.py
"""
Banshee creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=banshee
"""
from creature_base import GlobalCreatureBaseClass


class Banshee(GlobalCreatureBaseClass):
    """
    Banshee creature
    Size: Medium, Type: undead, chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 58,
        "min_level": 5,
        "level": 5,
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
        self.abilities.extend(['detect_life'])

    def detect_life(self) -> str:
        """Detect Life: The banshee can magically sense the presence of creatures up to 5 miles away that aren't undead or c..."""
        return "The banshee can magically sense the presence of creatures up to 5 miles away that aren't undead or constructs. She knows the general direction they're in but not their exact locations.Incorporeal Move"
    def detect_life(self) -> str:
        """Detect Life: The banshee can magically sense the presence of creatures up to 5 miles away that aren't undead or c..."""
        return "The banshee can magically sense the presence of creatures up to 5 miles away that aren't undead or constructs. She knows the general direction they're in but not their exact locations.Incorporeal Move"

