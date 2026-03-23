# bases1/owlbear.py
"""
Owlbear creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=owlbear
"""
from creature_base import GlobalCreatureBaseClass


class Owlbear(GlobalCreatureBaseClass):
    """
    Owlbear creature
    Size: Large, Type: monstrosity, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 59,
        "min_level": 4,
        "level": 4,
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
        self.abilities.extend(['keen_sight_and_smell'])

    def keen_sight_and_smell(self) -> str:
        """Keen Sight and Smell: The owlbear has advantage on Wisdom (Perception) checks that rely on sight or smell.ActionsMultiatta..."""
        return "The owlbear has advantage on Wisdom (Perception) checks that rely on sight or smell.ActionsMultiattack. The owlbear makes two attacks: one with its beak and one with its claws.Beak. Melee Weapon Attac"
    def keen_sight_and_smell(self) -> str:
        """Keen Sight and Smell: The owlbear has advantage on Wisdom (Perception) checks that rely on sight or smell.ActionsMultiatta..."""
        return "The owlbear has advantage on Wisdom (Perception) checks that rely on sight or smell.ActionsMultiattack. The owlbear makes two attacks: one with its beak and one with its claws.Beak. Melee Weapon Attac"

