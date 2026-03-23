# bases1/cradle-of-the-cloud-scion.py
"""
CradleOfTheCloudScion creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cradle-of-the-cloud-scion
"""
from creature_base import GlobalCreatureBaseClass


class CradleOfTheCloudScion(GlobalCreatureBaseClass):
    """
    CradleOfTheCloudScion creature
    Size: Gargantuan, Type: Elemental, typically Chaotic Neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 624,
        "min_level": 27,
        "level": 27,
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
        "type": "Elemental, typically Chaotic Neutral",
        "hit_points_up": [62, 62, 62],
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

