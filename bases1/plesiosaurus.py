# bases1/plesiosaurus.py
"""
Plesiosaurus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=plesiosaurus
"""
from creature_base import GlobalCreatureBaseClass


class Plesiosaurus(GlobalCreatureBaseClass):
    """
    Plesiosaurus creature
    Size: Large, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 68,
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
        "size": "Large",
        "type": "beast, unaligned",
        "hit_points_up": [6, 6, 6],
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
        self.abilities.extend(['hold_breath'])

    def hold_breath(self) -> str:
        """Hold Breath: The plesiosaurus can hold its breath for 1 hour.ActionsBite. Melee Weapon Attack: +6 to hit, reach 1..."""
        return "The plesiosaurus can hold its breath for 1 hour.ActionsBite. Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 14 (3d6 + 4) piercing damage.This predatory marine reptile and cousin to the"
    def hold_breath(self) -> str:
        """Hold Breath: The plesiosaurus can hold its breath for 1 hour.ActionsBite. Melee Weapon Attack: +6 to hit, reach 1..."""
        return "The plesiosaurus can hold its breath for 1 hour.ActionsBite. Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 14 (3d6 + 4) piercing damage.This predatory marine reptile and cousin to the"

