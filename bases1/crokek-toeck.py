# bases1/crokek-toeck.py
"""
CrokekToeck creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=crokek-toeck
"""
from creature_base import GlobalCreatureBaseClass


class CrokekToeck(GlobalCreatureBaseClass):
    """
    CrokekToeck creature
    Size: Gargantuan, Type: fiend (Demon), chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 297,
        "min_level": 15,
        "level": 15,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Gargantuan",
        "type": "fiend (Demon), chaotic evil",
        "hit_points_up": [29, 29, 29],
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

