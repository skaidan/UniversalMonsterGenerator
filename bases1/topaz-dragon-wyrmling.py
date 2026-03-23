# bases1/topaz-dragon-wyrmling.py
"""
TopazDragonWyrmling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=topaz-dragon-wyrmling
"""
from creature_base import GlobalCreatureBaseClass


class TopazDragonWyrmling(GlobalCreatureBaseClass):
    """
    TopazDragonWyrmling creature
    Size: Medium, Type: dragon (Gem), typically Chaotic Neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 33,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 16,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "dragon (Gem), typically Chaotic Neutral",
        "hit_points_up": [3, 3, 3],
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

