# bases1/worg.py
"""
Worg creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=worg
"""
from creature_base import GlobalCreatureBaseClass


class Worg(GlobalCreatureBaseClass):
    """
    Worg creature
    Size: Large, Type: monstrosity, neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 26,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "monstrosity, neutral evil",
        "hit_points_up": [2, 2, 2],
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
        self.abilities.extend(['keen_hearing_and_smell'])

    def keen_hearing_and_smell(self) -> str:
        """Keen Hearing and Smell: The worg has advantage on Wisdom (Perception) checks that rely on hearing or smell.ActionsBite. Mele..."""
        return "The worg has advantage on Wisdom (Perception) checks that rely on hearing or smell.ActionsBite. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) piercing damage. If the targe"
    def keen_hearing_and_smell(self) -> str:
        """Keen Hearing and Smell: The worg has advantage on Wisdom (Perception) checks that rely on hearing or smell.ActionsBite. Mele..."""
        return "The worg has advantage on Wisdom (Perception) checks that rely on hearing or smell.ActionsBite. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) piercing damage. If the targe"

