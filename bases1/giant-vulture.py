# bases1/giant-vulture.py
"""
GiantVulture creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-vulture
"""
from creature_base import GlobalCreatureBaseClass


class GiantVulture(GlobalCreatureBaseClass):
    """
    GiantVulture creature
    Size: Large, Type: beast, neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 22,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 10,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "beast, neutral evil",
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
        self.abilities.extend(['keen_sight_and_smell'])

    def keen_sight_and_smell(self) -> str:
        """Keen Sight and Smell: The vulture has advantage on Wisdom (Perception) checks that rely on sight or smell.Pack Tactics. Th..."""
        return "The vulture has advantage on Wisdom (Perception) checks that rely on sight or smell.Pack Tactics. The vulture has advantage on an attack roll against a creature if at least one of the vulture's allies"
    def keen_sight_and_smell(self) -> str:
        """Keen Sight and Smell: The vulture has advantage on Wisdom (Perception) checks that rely on sight or smell.Pack Tactics. Th..."""
        return "The vulture has advantage on Wisdom (Perception) checks that rely on sight or smell.Pack Tactics. The vulture has advantage on an attack roll against a creature if at least one of the vulture's allies"

