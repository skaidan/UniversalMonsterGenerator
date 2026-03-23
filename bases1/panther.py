# bases1/panther.py
"""
Panther creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=panther
"""
from creature_base import GlobalCreatureBaseClass


class Panther(GlobalCreatureBaseClass):
    """
    Panther creature
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
        self.abilities.extend(['keen_smell'])

    def keen_smell(self) -> str:
        """Keen Smell: The panther has advantage on Wisdom (Perception) checks that rely on smell.Pounce. If the panther mo..."""
        return "The panther has advantage on Wisdom (Perception) checks that rely on smell.Pounce. If the panther moves at least 20 feet straight toward a creature and then hits it with a claw attack on the same turn"
    def keen_smell(self) -> str:
        """Keen Smell: The panther has advantage on Wisdom (Perception) checks that rely on smell.Pounce. If the panther mo..."""
        return "The panther has advantage on Wisdom (Perception) checks that rely on smell.Pounce. If the panther moves at least 20 feet straight toward a creature and then hits it with a claw attack on the same turn"

