# bases1/mouth-of-grolantor.py
"""
MouthOfGrolantor creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mouth-of-grolantor
"""
from creature_base import GlobalCreatureBaseClass


class MouthOfGrolantor(GlobalCreatureBaseClass):
    """
    MouthOfGrolantor creature
    Size: Huge, Type: Giant, typically Chaotic Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 105,
        "min_level": 7,
        "level": 7,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "Giant, typically Chaotic Evil",
        "hit_points_up": [10, 10, 10],
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

