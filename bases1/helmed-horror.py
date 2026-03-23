# bases1/helmed-horror.py
"""
HelmedHorror creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=helmed-horror
"""
from creature_base import GlobalCreatureBaseClass


class HelmedHorror(GlobalCreatureBaseClass):
    """
    HelmedHorror creature
    Size: Medium, Type: construct, neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 60,
        "min_level": 5,
        "level": 5,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 20,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "construct, neutral",
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
        self.abilities.extend(['magic_resistance'])

    def magic_resistance(self) -> str:
        """Magic Resistance: The helmed horror has advantage on saving throws against spells and other magical effects.Spell Immu..."""
        return "The helmed horror has advantage on saving throws against spells and other magical effects.Spell Immunity. The helmed horror is immune to three spells chosen by its creator. Typical immunities include "
    def magic_resistance(self) -> str:
        """Magic Resistance: The helmed horror has advantage on saving throws against spells and other magical effects.Spell Immu..."""
        return "The helmed horror has advantage on saving throws against spells and other magical effects.Spell Immunity. The helmed horror is immune to three spells chosen by its creator. Typical immunities include "

