# bases1/mastiff.py
"""
Mastiff creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mastiff
"""
from creature_base import GlobalCreatureBaseClass


class Mastiff(GlobalCreatureBaseClass):
    """
    Mastiff creature
    Size: Medium, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 5,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "beast, unaligned",
        "hit_points_up": [1, 1, 1],
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
        """Keen Hearing and Smell: The mastiff has advantage on Wisdom (Perception) checks that rely on hearing or smell.ActionsBite. M..."""
        return "The mastiff has advantage on Wisdom (Perception) checks that rely on hearing or smell.ActionsBite. Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) piercing damage. If the tar"
    def keen_hearing_and_smell(self) -> str:
        """Keen Hearing and Smell: The mastiff has advantage on Wisdom (Perception) checks that rely on hearing or smell.ActionsBite. M..."""
        return "The mastiff has advantage on Wisdom (Perception) checks that rely on hearing or smell.ActionsBite. Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) piercing damage. If the tar"

