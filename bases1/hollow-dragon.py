# bases1/hollow-dragon.py
"""
HollowDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hollow-dragon
"""
from creature_base import GlobalCreatureBaseClass


class HollowDragon(GlobalCreatureBaseClass):
    """
    HollowDragon creature
    Size: Huge, Type: Undead, any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 241,
        "min_level": 19,
        "level": 19,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 19,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "Undead, any alignment",
        "hit_points_up": [24, 24, 24],
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

