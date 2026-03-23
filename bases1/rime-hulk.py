# bases1/rime-hulk.py
"""
RimeHulk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=rime-hulk
"""
from creature_base import GlobalCreatureBaseClass


class RimeHulk(GlobalCreatureBaseClass):
    """
    RimeHulk creature
    Size: Large, Type: Elemental, typically Neutral Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 85,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "Elemental, typically Neutral Evil",
        "hit_points_up": [8, 8, 8],
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

