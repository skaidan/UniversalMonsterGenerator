# bases1/tortle-druid.py
"""
TortleDruid creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=tortle-druid
"""
from creature_base import GlobalCreatureBaseClass


class TortleDruid(GlobalCreatureBaseClass):
    """
    TortleDruid creature
    Size: Medium, Type: Humanoid, any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 33,
        "min_level": 3,
        "level": 3,
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
        # Add creature-specific abilities
        self.abilities.extend(['hold_breath'])

    def hold_breath(self) -> str:
        """Hold Breath: The tortle can hold its breath for 1 hour.ActionsMultiattack. The tortle makes four Claw attacks or ..."""
        return "The tortle can hold its breath for 1 hour.ActionsMultiattack. The tortle makes four Claw attacks or two Nature's Wrath attacks.Claw. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d"

