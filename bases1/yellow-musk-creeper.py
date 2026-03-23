# bases1/yellow-musk-creeper.py
"""
YellowMuskCreeper creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yellow-musk-creeper
"""
from creature_base import GlobalCreatureBaseClass


class YellowMuskCreeper(GlobalCreatureBaseClass):
    """
    YellowMuskCreeper creature
    Size: Medium, Type: plant, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 60,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 6,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "plant, unaligned",
        "hit_points_up": [6, 6, 6],
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

