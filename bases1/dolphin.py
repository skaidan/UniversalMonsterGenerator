# bases1/dolphin.py
"""
Dolphin creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dolphin
"""
from creature_base import GlobalCreatureBaseClass


class Dolphin(GlobalCreatureBaseClass):
    """
    Dolphin creature
    Size: Medium, Type: Beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 11,
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
        "size": "Medium",
        "type": "Beast, unaligned",
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
        self.abilities.extend(['hold_breath'])

    def hold_breath(self) -> str:
        """Hold Breath: The dolphin can hold its breath for 20 minutes.ActionsSlam. Melee Weapon Attack: +4 to hit, reach 5 ..."""
        return "The dolphin can hold its breath for 20 minutes.ActionsSlam. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) bludgeoning damage. If the dolphin moved at least 30 feet straight"

