# bases1/cradle-of-the-fire-scion.py
"""
CradleOfTheFireScion creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cradle-of-the-fire-scion
"""
from creature_base import GlobalCreatureBaseClass


class CradleOfTheFireScion(GlobalCreatureBaseClass):
    """
    CradleOfTheFireScion creature
    Size: Gargantuan, Type: Elemental, typically Lawful Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 555,
        "min_level": 26,
        "level": 26,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 20,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Gargantuan",
        "type": "Elemental, typically Lawful Evil",
        "hit_points_up": [55, 55, 55],
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

