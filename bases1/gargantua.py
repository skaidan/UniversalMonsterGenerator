# bases1/gargantua.py
"""
Gargantua creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gargantua
"""
from creature_base import GlobalCreatureBaseClass


class Gargantua(GlobalCreatureBaseClass):
    """
    Gargantua creature
    Size: Gargantuan, Type: Aberration, typically Chaotic Neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 388,
        "min_level": 22,
        "level": 22,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Gargantuan",
        "type": "Aberration, typically Chaotic Neutral",
        "hit_points_up": [38, 38, 38],
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

