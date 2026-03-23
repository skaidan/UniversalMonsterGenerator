# bases1/ancient-dragon-turtle.py
"""
AncientDragonTurtle creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ancient-dragon-turtle
"""
from creature_base import GlobalCreatureBaseClass


class AncientDragonTurtle(GlobalCreatureBaseClass):
    """
    AncientDragonTurtle creature
    Size: Gargantuan, Type: Dragon, typically Neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 409,
        "min_level": 25,
        "level": 25,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 22,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Gargantuan",
        "type": "Dragon, typically Neutral",
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

