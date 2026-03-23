# bases1/derro-savant.py
"""
DerroSavant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=derro-savant
"""
from creature_base import GlobalCreatureBaseClass


class DerroSavant(GlobalCreatureBaseClass):
    """
    DerroSavant creature
    Size: Small, Type: Aberration (Sorcerer), typically Chaotic Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 36,
        "min_level": 4,
        "level": 4,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Small",
        "type": "Aberration (Sorcerer), typically Chaotic Evil",
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
        self.abilities.extend(['magic_resistance'])

    def magic_resistance(self) -> str:
        """Magic Resistance: The derro has advantage on saving throws against spells and other magical effects.Sunlight Sensitivi..."""
        return "The derro has advantage on saving throws against spells and other magical effects.Sunlight Sensitivity. While in sunlight, the derro has disadvantage on attack rolls, as well as on Wisdom (Perception)"

