# bases1/giant-eagle.py
"""
GiantEagle creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-eagle
"""
from creature_base import GlobalCreatureBaseClass


class GiantEagle(GlobalCreatureBaseClass):
    """
    GiantEagle creature
    Size: Large, Type: beast, neutral good
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
        "type": "beast, neutral good",
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
        self.abilities.extend(['keen_sight'])

    def keen_sight(self) -> str:
        """Keen Sight: The eagle has advantage on Wisdom (Perception) checks that rely on sight.ActionsMultiattack. The eag..."""
        return "The eagle has advantage on Wisdom (Perception) checks that rely on sight.ActionsMultiattack. The eagle makes two attacks: one with its beak and one with its talons.Beak. Melee Weapon Attack: +5 to hit"
    def keen_sight(self) -> str:
        """Keen Sight: The eagle has advantage on Wisdom (Perception) checks that rely on sight.ActionsMultiattack. The eag..."""
        return "The eagle has advantage on Wisdom (Perception) checks that rely on sight.ActionsMultiattack. The eagle makes two attacks: one with its beak and one with its talons.Beak. Melee Weapon Attack: +5 to hit"

