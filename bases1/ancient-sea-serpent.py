# bases1/ancient-sea-serpent.py
"""
AncientSeaSerpent creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ancient-sea-serpent
"""
from creature_base import GlobalCreatureBaseClass


class AncientSeaSerpent(GlobalCreatureBaseClass):
    """
    AncientSeaSerpent creature
    Size: Gargantuan, Type: Dragon, typically Neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 170,
        "min_level": 15,
        "level": 15,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Gargantuan",
        "type": "Dragon, typically Neutral",
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

