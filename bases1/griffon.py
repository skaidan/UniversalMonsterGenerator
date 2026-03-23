# bases1/griffon.py
"""
Griffon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=griffon
"""
from creature_base import GlobalCreatureBaseClass


class Griffon(GlobalCreatureBaseClass):
    """
    Griffon creature
    Size: Large, Type: monstrosity, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 59,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "monstrosity, unaligned",
        "hit_points_up": [5, 5, 5],
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
        """Keen Sight: The griffon has advantage on Wisdom (Perception) checks that rely on sight.ActionsMultiattack. The g..."""
        return "The griffon has advantage on Wisdom (Perception) checks that rely on sight.ActionsMultiattack. The griffon makes two attacks: one with its beak and one with its claws.Beak. Melee Weapon Attack: +6 to "
    def keen_sight(self) -> str:
        """Keen Sight: The griffon has advantage on Wisdom (Perception) checks that rely on sight.ActionsMultiattack. The g..."""
        return "The griffon has advantage on Wisdom (Perception) checks that rely on sight.ActionsMultiattack. The griffon makes two attacks: one with its beak and one with its claws.Beak. Melee Weapon Attack: +6 to "

