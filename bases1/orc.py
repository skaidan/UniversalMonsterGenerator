# bases1/orc.py
"""
Orc creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=orc
"""
from creature_base import GlobalCreatureBaseClass


class Orc(GlobalCreatureBaseClass):
    """
    Orc creature
    Size: Medium, Type: humanoid (Orc), chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 15,
        "min_level": 2,
        "level": 2,
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
        "type": "humanoid (Orc), chaotic evil",
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
        self.abilities.extend(['aggressive'])

    def aggressive(self) -> str:
        """Aggressive: As a bonus action, the orc can move up to its speed toward a hostile creature that it can see.Action..."""
        return "As a bonus action, the orc can move up to its speed toward a hostile creature that it can see.ActionsGreataxe. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 9 (1d12 + 3) slashing damag"
    def aggressive(self) -> str:
        """Aggressive: As a bonus action, the orc can move up to its speed toward a hostile creature that it can see.Action..."""
        return "As a bonus action, the orc can move up to its speed toward a hostile creature that it can see.ActionsGreataxe. Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 9 (1d12 + 3) slashing damag"

