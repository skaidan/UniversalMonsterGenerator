# bases1/tanarukk.py
"""
Tanarukk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=tanarukk
"""
from creature_base import GlobalCreatureBaseClass


class Tanarukk(GlobalCreatureBaseClass):
    """
    Tanarukk creature
    Size: Medium, Type: Fiend (Demon), typically Chaotic Evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 95,
        "min_level": 6,
        "level": 6,
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
        "type": "Fiend (Demon), typically Chaotic Evil",
        "hit_points_up": [9, 9, 9],
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
        """Magic Resistance: The tanarukk has advantage on saving throws against spells and other magical effects.ActionsMultiatt..."""
        return "The tanarukk has advantage on saving throws against spells and other magical effects.ActionsMultiattack. The tanarukk makes one Bite attack and one Greatsword attack.Bite. Melee Weapon Attack: +7 to h"

