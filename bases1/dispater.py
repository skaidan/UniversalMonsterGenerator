# bases1/dispater.py
"""
Dispater creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dispater
"""
from creature_base import GlobalCreatureBaseClass


class Dispater(GlobalCreatureBaseClass):
    """
    Dispater creature
    Size: Large, Type: Fiend (Devil), Lawful Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 412,
        "min_level": 28,
        "level": 28,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 21,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "Fiend (Devil), Lawful Evil",
        "hit_points_up": [41, 41, 41],
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

