# bases1/scion-of-grolantor.py
"""
ScionOfGrolantor creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=scion-of-grolantor
"""
from creature_base import GlobalCreatureBaseClass


class ScionOfGrolantor(GlobalCreatureBaseClass):
    """
    ScionOfGrolantor creature
    Size: Gargantuan, Type: Giant (Titan), typically Chaotic Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 402,
        "min_level": 23,
        "level": 23,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 18,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Gargantuan",
        "type": "Giant (Titan), typically Chaotic Evil",
        "hit_points_up": [40, 40, 40],
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

