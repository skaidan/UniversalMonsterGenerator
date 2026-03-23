# bases1/young-remorhaz.py
"""
YoungRemorhaz creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=young-remorhaz
"""
from creature_base import GlobalCreatureBaseClass


class YoungRemorhaz(GlobalCreatureBaseClass):
    """
    YoungRemorhaz creature
    Size: Large, Type: monstrosity, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 93,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "monstrosity, unaligned",
        "hit_points_up": [9, 9, 9],
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
        self.abilities.extend(['heated_body'])

    def heated_body(self) -> str:
        """Heated Body: A creature that touches the remorhaz or hits it with a melee attack while within 5 feet of it takes ..."""
        return "A creature that touches the remorhaz or hits it with a melee attack while within 5 feet of it takes 7 (2d6) fire damage.ActionsBite. Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 20 (3"
    def heated_body(self) -> str:
        """Heated Body: A creature that touches the remorhaz or hits it with a melee attack while within 5 feet of it takes ..."""
        return "A creature that touches the remorhaz or hits it with a melee attack while within 5 feet of it takes 7 (2d6) fire damage.ActionsBite. Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 20 (3"

