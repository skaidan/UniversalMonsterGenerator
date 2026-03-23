# bases1/hungry-sorrowsworn.py
"""
HungrySorrowsworn creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hungry-sorrowsworn
"""
from creature_base import GlobalCreatureBaseClass


class HungrySorrowsworn(GlobalCreatureBaseClass):
    """
    HungrySorrowsworn creature
    Size: Medium, Type: Monstrosity, typically Neutral Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 225,
        "min_level": 12,
        "level": 12,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Monstrosity, typically Neutral Evil",
        "hit_points_up": [22, 22, 22],
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

