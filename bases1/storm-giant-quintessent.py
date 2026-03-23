# bases1/storm-giant-quintessent.py
"""
StormGiantQuintessent creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=storm-giant-quintessent
"""
from creature_base import GlobalCreatureBaseClass


class StormGiantQuintessent(GlobalCreatureBaseClass):
    """
    StormGiantQuintessent creature
    Size: Huge, Type: Giant, typically Chaotic Good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 230,
        "min_level": 17,
        "level": 17,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "Giant, typically Chaotic Good",
        "hit_points_up": [23, 23, 23],
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

