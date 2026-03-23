# bases1/baphomet.py
"""
Baphomet creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=baphomet
"""
from creature_base import GlobalCreatureBaseClass


class Baphomet(GlobalCreatureBaseClass):
    """
    Baphomet creature
    Size: Huge, Type: Fiend (Demon), Chaotic Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 319,
        "min_level": 24,
        "level": 24,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 22,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "Fiend (Demon), Chaotic Evil",
        "hit_points_up": [31, 31, 31],
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

