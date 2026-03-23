# bases1/troll.py
"""
Troll creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=troll
"""
from creature_base import GlobalCreatureBaseClass


class Troll(GlobalCreatureBaseClass):
    """
    Troll creature
    Size: Large, Type: giant, chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 84,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "giant, chaotic evil",
        "hit_points_up": [8, 8, 8],
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
        """Keen Smell: The troll has advantage on Wisdom (Perception) checks that rely on smell.Regeneration. The troll reg..."""
        return "The troll has advantage on Wisdom (Perception) checks that rely on smell.Regeneration. The troll regains 10 hit points at the start of its turn. If the troll takes acid or fire damage, this trait does"
    def keen_smell(self) -> str:
        """Keen Smell: The troll has advantage on Wisdom (Perception) checks that rely on smell.Regeneration. The troll reg..."""
        return "The troll has advantage on Wisdom (Perception) checks that rely on smell.Regeneration. The troll regains 10 hit points at the start of its turn. If the troll takes acid or fire damage, this trait does"

