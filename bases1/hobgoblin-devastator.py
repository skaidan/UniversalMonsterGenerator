# bases1/hobgoblin-devastator.py
"""
HobgoblinDevastator creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hobgoblin-devastator
"""
from creature_base import GlobalCreatureBaseClass


class HobgoblinDevastator(GlobalCreatureBaseClass):
    """
    HobgoblinDevastator creature
    Size: Medium, Type: Fey (Goblinoid), typically Lawful Neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 45,
        "min_level": 5,
        "level": 5,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Fey (Goblinoid), typically Lawful Neutral",
        "hit_points_up": [4, 4, 4],
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

