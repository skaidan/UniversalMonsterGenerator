# bases1/glasya.py
"""
Glasya creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=glasya
"""
from creature_base import GlobalCreatureBaseClass


class Glasya(GlobalCreatureBaseClass):
    """
    Glasya creature
    Size: Medium, Type: Fiend (Devil), Lawful Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 380,
        "min_level": 26,
        "level": 26,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 21,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Fiend (Devil), Lawful Evil",
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

