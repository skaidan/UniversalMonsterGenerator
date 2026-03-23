# bases1/cradle-of-the-storm-scion.py
"""
CradleOfTheStormScion creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cradle-of-the-storm-scion
"""
from creature_base import GlobalCreatureBaseClass


class CradleOfTheStormScion(GlobalCreatureBaseClass):
    """
    CradleOfTheStormScion creature
    Size: Gargantuan, Type: Elemental, typically Chaotic Good
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 682,
        "min_level": 28,
        "level": 28,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 19,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Gargantuan",
        "type": "Elemental, typically Chaotic Good",
        "hit_points_up": [68, 68, 68],
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

