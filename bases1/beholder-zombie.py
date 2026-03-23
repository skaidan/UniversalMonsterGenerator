# bases1/beholder-zombie.py
"""
BeholderZombie creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=beholder-zombie
"""
from creature_base import GlobalCreatureBaseClass


class BeholderZombie(GlobalCreatureBaseClass):
    """
    BeholderZombie creature
    Size: Large, Type: undead, neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 93,
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
        "type": "undead, neutral evil",
        "hit_points_up": [9, 9, 9],
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
        """Undead Fortitude: If damage reduces the zombie to 0 Hit Points, it makes a Constitution saving throw (DC 5 plus the da..."""
        return "If damage reduces the zombie to 0 Hit Points, it makes a Constitution saving throw (DC 5 plus the damage taken) unless the damage is Radiant or from a Critical Hit. On a successful save, the zombie dr"
    def undead_fortitude(self) -> str:
        """Undead Fortitude: If damage reduces the zombie to 0 Hit Points, it makes a Constitution saving throw (DC 5 plus the da..."""
        return "If damage reduces the zombie to 0 Hit Points, it makes a Constitution saving throw (DC 5 plus the damage taken) unless the damage is Radiant or from a Critical Hit. On a successful save, the zombie dr"

