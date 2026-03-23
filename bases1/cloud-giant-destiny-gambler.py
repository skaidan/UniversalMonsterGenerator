# bases1/cloud-giant-destiny-gambler.py
"""
CloudGiantDestinyGambler creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cloud-giant-destiny-gambler
"""
from creature_base import GlobalCreatureBaseClass


class CloudGiantDestinyGambler(GlobalCreatureBaseClass):
    """
    CloudGiantDestinyGambler creature
    Size: Huge, Type: Giant (Bard), any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 337,
        "min_level": 20,
        "level": 20,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "Giant (Bard), any alignment",
        "hit_points_up": [33, 33, 33],
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

