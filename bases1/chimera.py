# bases1/chimera.py
"""
Chimera creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=chimera
"""
from creature_base import GlobalCreatureBaseClass


class Chimera(GlobalCreatureBaseClass):
    """
    Chimera creature
    Size: Large, Type: monstrosity, chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 114,
        "min_level": 7,
        "level": 7,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 14,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "monstrosity, chaotic evil",
        "hit_points_up": [11, 11, 11],
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
        self.abilities.extend(['multiattack'])

    def multiattack(self) -> str:
        """Multiattack: The chimera makes three attacks: one with its bite, one with its horns, and one with its claws. When..."""
        return "The chimera makes three attacks: one with its bite, one with its horns, and one with its claws. When its fire breath is available, it can use the breath in place of its bite or horns.Bite. Melee Weapo"
    def multiattack(self) -> str:
        """Multiattack: The chimera makes three attacks: one with its bite, one with its horns, and one with its claws. When..."""
        return "The chimera makes three attacks: one with its bite, one with its horns, and one with its claws. When its fire breath is available, it can use the breath in place of its bite or horns.Bite. Melee Weapo"

