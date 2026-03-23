# bases1/giant-owl.py
"""
GiantOwl creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-owl
"""
from creature_base import GlobalCreatureBaseClass


class GiantOwl(GlobalCreatureBaseClass):
    """
    GiantOwl creature
    Size: Large, Type: beast, neutral
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
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "beast, neutral",
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
        self.abilities.extend(['flyby'])

    def flyby(self) -> str:
        """Flyby: The owl doesn't provoke opportunity attacks when it flies out of an enemy's reach.Keen Hearing and S..."""
        return "The owl doesn't provoke opportunity attacks when it flies out of an enemy's reach.Keen Hearing and Sight. The owl has advantage on Wisdom (Perception) checks that rely on hearing or sight.ActionsTalon"
    def flyby(self) -> str:
        """Flyby: The owl doesn't provoke opportunity attacks when it flies out of an enemy's reach.Keen Hearing and S..."""
        return "The owl doesn't provoke opportunity attacks when it flies out of an enemy's reach.Keen Hearing and Sight. The owl has advantage on Wisdom (Perception) checks that rely on hearing or sight.ActionsTalon"

