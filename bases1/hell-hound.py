# bases1/hell-hound.py
"""
HellHound creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hell-hound
"""
from creature_base import GlobalCreatureBaseClass


class HellHound(GlobalCreatureBaseClass):
    """
    HellHound creature
    Size: Medium, Type: fiend, lawful evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 45,
        "min_level": 4,
        "level": 4,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "fiend, lawful evil",
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
        self.abilities.extend(['keen_hearing_and_smell'])

    def keen_hearing_and_smell(self) -> str:
        """Keen Hearing and Smell: The hound has advantage on Wisdom (Perception) checks that rely on hearing or smell.Pack Tactics. Th..."""
        return "The hound has advantage on Wisdom (Perception) checks that rely on hearing or smell.Pack Tactics. The hound has advantage on an attack roll against a creature if at least one of the hound's allies is "
    def keen_hearing_and_smell(self) -> str:
        """Keen Hearing and Smell: The hound has advantage on Wisdom (Perception) checks that rely on hearing or smell.Pack Tactics. Th..."""
        return "The hound has advantage on Wisdom (Perception) checks that rely on hearing or smell.Pack Tactics. The hound has advantage on an attack roll against a creature if at least one of the hound's allies is "

