# bases1/cloud-giant-of-evil-air.py
"""
CloudGiantOfEvilAir creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cloud-giant-of-evil-air
"""
from creature_base import GlobalCreatureBaseClass


class CloudGiantOfEvilAir(GlobalCreatureBaseClass):
    """
    CloudGiantOfEvilAir creature
    Size: Huge, Type: Giant, typically Neutral Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 200,
        "min_level": 13,
        "level": 13,
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
        "type": "Giant, typically Neutral Evil",
        "hit_points_up": [20, 20, 20],
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

