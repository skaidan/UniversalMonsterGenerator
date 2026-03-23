# bases1/tortle.py
"""
Tortle creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=tortle
"""
from creature_base import GlobalCreatureBaseClass


class Tortle(GlobalCreatureBaseClass):
    """
    Tortle creature
    Size: Medium, Type: Humanoid, any alignment
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
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "Humanoid, any alignment",
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
        # Add creature-specific abilities
        self.abilities.extend(['hold_breath'])

    def hold_breath(self) -> str:
        """Hold Breath: The tortle can hold its breath for 1 hour.ActionsClaw. Melee Weapon Attack: +4 to hit, reach 5 ft., ..."""
        return "The tortle can hold its breath for 1 hour.ActionsClaw. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage.Spear. Melee or Ranged Weapon Attack: +4 to hit, reach "

