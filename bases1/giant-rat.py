# bases1/giant-rat.py
"""
GiantRat creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-rat
"""
from creature_base import GlobalCreatureBaseClass


class GiantRat(GlobalCreatureBaseClass):
    """
    GiantRat creature
    Size: Small, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 7,
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
        "size": "Small",
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
        """Keen Smell: The rat has advantage on Wisdom (Perception) checks that rely on smell.Pack Tactics. The rat has adv..."""
        return "The rat has advantage on Wisdom (Perception) checks that rely on smell.Pack Tactics. The rat has advantage on an attack roll against a creature if at least one of the rat's allies is within 5 feet of "
    def keen_smell(self) -> str:
        """Keen Smell: The rat has advantage on Wisdom (Perception) checks that rely on smell.Pack Tactics. The rat has adv..."""
        return "The rat has advantage on Wisdom (Perception) checks that rely on smell.Pack Tactics. The rat has advantage on an attack roll against a creature if at least one of the rat's allies is within 5 feet of "

