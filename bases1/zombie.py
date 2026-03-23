# bases1/zombie.py
"""
Zombie creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=zombie
"""
from creature_base import GlobalCreatureBaseClass


class Zombie(GlobalCreatureBaseClass):
    """
    Zombie creature
    Size: Medium, Type: undead, neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 22,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 8,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "undead, neutral evil",
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
        self.abilities.extend(['undead_fortitude'])

    def undead_fortitude(self) -> str:
        """Undead Fortitude: If damage reduces the zombie to 0 hit points, it must make a Constitution saving throw with a DC of ..."""
        return "If damage reduces the zombie to 0 hit points, it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant or from a critical hit. On a success, the zombie "
    def undead_fortitude(self) -> str:
        """Undead Fortitude: If damage reduces the zombie to 0 hit points, it must make a Constitution saving throw with a DC of ..."""
        return "If damage reduces the zombie to 0 hit points, it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant or from a critical hit. On a success, the zombie "

