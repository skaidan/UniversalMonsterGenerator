# bases1/neothelid.py
"""
Neothelid creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=neothelid
"""
from creature_base import GlobalCreatureBaseClass


class Neothelid(GlobalCreatureBaseClass):
    """
    Neothelid creature
    Size: Gargantuan, Type: Aberration, typically Chaotic Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 232,
        "min_level": 14,
        "level": 14,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 16,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Gargantuan",
        "type": "Aberration, typically Chaotic Evil",
        "hit_points_up": [23, 23, 23],
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

