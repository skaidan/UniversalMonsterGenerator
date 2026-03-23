# bases1/quaggoth.py
"""
Quaggoth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=quaggoth
"""
from creature_base import GlobalCreatureBaseClass


class Quaggoth(GlobalCreatureBaseClass):
    """
    Quaggoth creature
    Size: Medium, Type: humanoid (Quaggoth), chaotic neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 45,
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
        "type": "humanoid (Quaggoth), chaotic neutral",
        "hit_points_up": [4, 4, 4],
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
        self.abilities.extend(['wounded_fury'])

    def wounded_fury(self) -> str:
        """Wounded Fury: While it has 10 hit points or fewer, the quaggoth has advantage on attack rolls. In addition, it dea..."""
        return "While it has 10 hit points or fewer, the quaggoth has advantage on attack rolls. In addition, it deals an extra 7 (2d6) damage to any target it hits with a melee attack.ActionsMultiattack. The quaggot"
    def wounded_fury(self) -> str:
        """Wounded Fury: While it has 10 hit points or fewer, the quaggoth has advantage on attack rolls. In addition, it dea..."""
        return "While it has 10 hit points or fewer, the quaggoth has advantage on attack rolls. In addition, it deals an extra 7 (2d6) damage to any target it hits with a melee attack.ActionsMultiattack. The quaggot"

