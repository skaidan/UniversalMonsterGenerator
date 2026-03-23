# bases1/derro.py
"""
Derro creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=derro
"""
from creature_base import GlobalCreatureBaseClass


class Derro(GlobalCreatureBaseClass):
    """
    Derro creature
    Size: Medium, Type: or smaller, the derro can choose to deal no damage and knock it prone.
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
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "or smaller, the derro can choose to deal no damage and knock it prone.",
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
        self.abilities.extend(['magic_resistance'])

    def magic_resistance(self) -> str:
        """Magic Resistance: The derro has advantage on saving throws against spells and other magical effects.Sunlight Sensitivi..."""
        return "The derro has advantage on saving throws against spells and other magical effects.Sunlight Sensitivity. While in sunlight, the derro has disadvantage on attack rolls, as well as on Wisdom (Perception)"

