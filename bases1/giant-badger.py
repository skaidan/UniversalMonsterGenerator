# bases1/giant-badger.py
"""
GiantBadger creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-badger
"""
from creature_base import GlobalCreatureBaseClass


class GiantBadger(GlobalCreatureBaseClass):
    """
    GiantBadger creature
    Size: Medium, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 13,
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
        self.abilities.extend(['keen_smell'])

    def keen_smell(self) -> str:
        """Keen Smell: The badger has advantage on Wisdom (Perception) checks that rely on smell.ActionsMultiattack. The ba..."""
        return "The badger has advantage on Wisdom (Perception) checks that rely on smell.ActionsMultiattack. The badger makes two attacks: one with its bite and one with its claws.Bite. Melee Weapon Attack: +3 to hi"
    def keen_smell(self) -> str:
        """Keen Smell: The badger has advantage on Wisdom (Perception) checks that rely on smell.ActionsMultiattack. The ba..."""
        return "The badger has advantage on Wisdom (Perception) checks that rely on smell.ActionsMultiattack. The badger makes two attacks: one with its bite and one with its claws.Bite. Melee Weapon Attack: +3 to hi"

