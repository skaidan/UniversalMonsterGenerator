# bases1/steel-defender.py
"""
SteelDefender creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=steel-defender
"""
from creature_base import GlobalCreatureBaseClass


class SteelDefender(GlobalCreatureBaseClass):
    """
    SteelDefender creature
    Size: Medium, Type: construct, -
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 2,
        "min_level": 1,
        "level": 1,
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
        "type": "construct, -",
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
        self.abilities.extend(['vigilant'])

    def vigilant(self) -> str:
        """Vigilant: The defender can't be surprised.ActionsForce-Empowered Rend. Melee Weapon Attack: your spell attack ..."""
        return "The defender can't be surprised.ActionsForce-Empowered Rend. Melee Weapon Attack: your spell attack modifier to hit, reach 5 ft., one target you can see. Hit: 1d8 + PB force damage.Repair (3/Day). The"

