# bases1/nalfeshnee.py
"""
Nalfeshnee creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=nalfeshnee
"""
from creature_base import GlobalCreatureBaseClass


class Nalfeshnee(GlobalCreatureBaseClass):
    """
    Nalfeshnee creature
    Size: Large, Type: fiend (Demon), chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 184,
        "min_level": 14,
        "level": 14,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 18,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "fiend (Demon), chaotic evil",
        "hit_points_up": [18, 18, 18],
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
        """Magic Resistance: The nalfeshnee has advantage on saving throws against spells and other magical effects.ActionsMultia..."""
        return "The nalfeshnee has advantage on saving throws against spells and other magical effects.ActionsMultiattack. The nalfeshnee uses Horror Nimbus if it can. It then makes three attacks: one with its bite a"
    def magic_resistance(self) -> str:
        """Magic Resistance: The nalfeshnee has advantage on saving throws against spells and other magical effects.ActionsMultia..."""
        return "The nalfeshnee has advantage on saving throws against spells and other magical effects.ActionsMultiattack. The nalfeshnee uses Horror Nimbus if it can. It then makes three attacks: one with its bite a"

