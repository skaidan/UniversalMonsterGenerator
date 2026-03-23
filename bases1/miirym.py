# bases1/miirym.py
"""
Miirym creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=miirym
"""
from creature_base import GlobalCreatureBaseClass


class Miirym(GlobalCreatureBaseClass):
    """
    Miirym creature
    Size: Large, Type: undead, -
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 262,
        "min_level": 23,
        "level": 23,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 10,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "undead, -",
        "hit_points_up": [26, 26, 26],
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
        # No special abilities

