# bases1/hippogriff.py
"""
Hippogriff creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hippogriff
"""
from creature_base import GlobalCreatureBaseClass


class Hippogriff(GlobalCreatureBaseClass):
    """
    Hippogriff creature
    Size: Large, Type: monstrosity, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 19,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 11,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "monstrosity, unaligned",
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
        self.abilities.extend(['keen_sight'])

    def keen_sight(self) -> str:
        """Keen Sight: The hippogriff has advantage on Wisdom (Perception) checks that rely on sight.ActionsMultiattack. Th..."""
        return "The hippogriff has advantage on Wisdom (Perception) checks that rely on sight.ActionsMultiattack. The hippogriff makes two attacks: one with its beak and one with its claws.Beak. Melee Weapon Attack: "
    def keen_sight(self) -> str:
        """Keen Sight: The hippogriff has advantage on Wisdom (Perception) checks that rely on sight.ActionsMultiattack. Th..."""
        return "The hippogriff has advantage on Wisdom (Perception) checks that rely on sight.ActionsMultiattack. The hippogriff makes two attacks: one with its beak and one with its claws.Beak. Melee Weapon Attack: "

