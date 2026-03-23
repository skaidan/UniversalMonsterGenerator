# bases1/ogre-zombie.py
"""
OgreZombie creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ogre-zombie
"""
from creature_base import GlobalCreatureBaseClass


class OgreZombie(GlobalCreatureBaseClass):
    """
    OgreZombie creature
    Size: Large, Type: undead, neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 85,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 8,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "undead, neutral evil",
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
        self.abilities.extend(['undead_fortitude'])

    def undead_fortitude(self) -> str:
        """Undead Fortitude: If damage reduces the zombie to 0 hit points, it must make a Constitution saving throw with a DC of ..."""
        return "If damage reduces the zombie to 0 hit points, it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant or from a critical hit. On a success, the zombie "
    def undead_fortitude(self) -> str:
        """Undead Fortitude: If damage reduces the zombie to 0 hit points, it must make a Constitution saving throw with a DC of ..."""
        return "If damage reduces the zombie to 0 hit points, it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant or from a critical hit. On a success, the zombie "

