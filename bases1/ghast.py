# bases1/ghast.py
"""
Ghast creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ghast
"""
from creature_base import GlobalCreatureBaseClass


class Ghast(GlobalCreatureBaseClass):
    """
    Ghast creature
    Size: Medium, Type: undead, chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 36,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "undead, chaotic evil",
        "hit_points_up": [3, 3, 3],
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
        self.abilities.extend(['stench'])

    def stench(self) -> str:
        """Stench: Any creature that starts its turn within 5 feet of the ghast must succeed on a DC 10 Constitution sa..."""
        return "Any creature that starts its turn within 5 feet of the ghast must succeed on a DC 10 Constitution saving throw or be poisoned until the start of its next turn. On a successful saving throw, the creatu"
    def stench(self) -> str:
        """Stench: Any creature that starts its turn within 5 feet of the ghast must succeed on a DC 10 Constitution sa..."""
        return "Any creature that starts its turn within 5 feet of the ghast must succeed on a DC 10 Constitution saving throw or be poisoned until the start of its next turn. On a successful saving throw, the creatu"

