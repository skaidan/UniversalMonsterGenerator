# bases1/giant-crab.py
"""
GiantCrab creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-crab
"""
from creature_base import GlobalCreatureBaseClass


class GiantCrab(GlobalCreatureBaseClass):
    """
    GiantCrab creature
    Size: Medium, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 13,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "beast, unaligned",
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
        self.abilities.extend(['amphibious'])

    def amphibious(self) -> str:
        """Amphibious: The crab can breathe air and water.ActionsClaw. Melee Weapon Attack: +3 to hit, reach 5 ft., one tar..."""
        return "The crab can breathe air and water.ActionsClaw. Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) bludgeoning damage, and the target is grappled (escape DC 11). The crab has tw"
    def amphibious(self) -> str:
        """Amphibious: The crab can breathe air and water.ActionsClaw. Melee Weapon Attack: +3 to hit, reach 5 ft., one tar..."""
        return "The crab can breathe air and water.ActionsClaw. Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) bludgeoning damage, and the target is grappled (escape DC 11). The crab has tw"

