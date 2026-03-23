# bases1/mummified-warrior.py
"""
MummifiedWarrior creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mummified-warrior
"""
from creature_base import GlobalCreatureBaseClass


class MummifiedWarrior(GlobalCreatureBaseClass):
    """
    MummifiedWarrior creature
    Size: Medium, Type: undead, neutral
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
        "armor_class": 8,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "undead, neutral",
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
        # Add creature-specific abilities
        self.abilities.extend(['undead_fortitude'])

    def undead_fortitude(self) -> str:
        """Undead Fortitude: If damage reduces the mummified warrior to 0 hit points, it must make a Constitution saving throw wi..."""
        return "If damage reduces the mummified warrior to 0 hit points, it must make a Constitution saving throw with a DC of 5 + the damage taken, unless the damage is radiant or from a critical hit. On a success, "

