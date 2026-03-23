# bases1/young-sea-serpent.py
"""
YoungSeaSerpent creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=young-sea-serpent
"""
from creature_base import GlobalCreatureBaseClass


class YoungSeaSerpent(GlobalCreatureBaseClass):
    """
    YoungSeaSerpent creature
    Size: Huge, Type: Dragon, typically Neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 123,
        "min_level": 9,
        "level": 9,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 16,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "Dragon, typically Neutral",
        "hit_points_up": [12, 12, 12],
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

