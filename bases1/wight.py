# bases1/wight.py
"""
Wight creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=wight
"""
from creature_base import GlobalCreatureBaseClass


class Wight(GlobalCreatureBaseClass):
    """
    Wight creature
    Size: Medium, Type: undead, neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 45,
        "min_level": 4,
        "level": 4,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "undead, neutral evil",
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
        self.abilities.extend(['sunlight_sensitivity'])

    def sunlight_sensitivity(self) -> str:
        """Sunlight Sensitivity: While in sunlight, the wight has disadvantage on attack rolls, as well as on Wisdom (Perception) che..."""
        return "While in sunlight, the wight has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight.ActionsMultiattack. The wight makes two longsword attacks or two longbow atta"
    def sunlight_sensitivity(self) -> str:
        """Sunlight Sensitivity: While in sunlight, the wight has disadvantage on attack rolls, as well as on Wisdom (Perception) che..."""
        return "While in sunlight, the wight has disadvantage on attack rolls, as well as on Wisdom (Perception) checks that rely on sight.ActionsMultiattack. The wight makes two longsword attacks or two longbow atta"

