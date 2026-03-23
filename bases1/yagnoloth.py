# bases1/yagnoloth.py
"""
Yagnoloth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yagnoloth
"""
from creature_base import GlobalCreatureBaseClass


class Yagnoloth(GlobalCreatureBaseClass):
    """
    Yagnoloth creature
    Size: Large, Type: Fiend (Yugoloth), typically Neutral Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 147,
        "min_level": 12,
        "level": 12,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "Fiend (Yugoloth), typically Neutral Evil",
        "hit_points_up": [14, 14, 14],
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
        """Magic Resistance: The yagnoloth has advantage on saving throws against spells and other magical effects.ActionsMultiat..."""
        return "The yagnoloth has advantage on saving throws against spells and other magical effects.ActionsMultiattack. The yagnoloth makes one Electrified Touch attack and one Massive Arm attack, or it makes one M"

