# bases1/wersten-kern.py
"""
WerstenKern creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=wersten-kern
"""
from creature_base import GlobalCreatureBaseClass


class WerstenKern(GlobalCreatureBaseClass):
    """
    WerstenKern creature
    Size: Medium, Type: Undead, Lawful Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 178,
        "min_level": 15,
        "level": 15,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 18,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Undead, Lawful Evil",
        "hit_points_up": [17, 17, 17],
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

