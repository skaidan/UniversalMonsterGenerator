# bases1/stone-giant-rockspeaker.py
"""
StoneGiantRockspeaker creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=stone-giant-rockspeaker
"""
from creature_base import GlobalCreatureBaseClass


class StoneGiantRockspeaker(GlobalCreatureBaseClass):
    """
    StoneGiantRockspeaker creature
    Size: Huge, Type: Giant (Wizard), any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 276,
        "min_level": 17,
        "level": 17,
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
        "type": "Giant (Wizard), any alignment",
        "hit_points_up": [27, 27, 27],
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

