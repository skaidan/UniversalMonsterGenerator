# bases1/zargon-the-returner.py
"""
ZargonTheReturner creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=zargon-the-returner
"""
from creature_base import GlobalCreatureBaseClass


class ZargonTheReturner(GlobalCreatureBaseClass):
    """
    ZargonTheReturner creature
    Size: Huge, Type: Aberration, Lawful Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 253,
        "min_level": 18,
        "level": 18,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 18,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "Aberration, Lawful Evil",
        "hit_points_up": [25, 25, 25],
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

