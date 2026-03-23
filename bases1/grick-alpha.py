# bases1/grick-alpha.py
"""
GrickAlpha creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=grick-alpha
"""
from creature_base import GlobalCreatureBaseClass


class GrickAlpha(GlobalCreatureBaseClass):
    """
    GrickAlpha creature
    Size: Large, Type: monstrosity, neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 75,
        "min_level": 8,
        "level": 8,
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
        "type": "monstrosity, neutral",
        "hit_points_up": [7, 7, 7],
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
        self.abilities.extend(['stone_camouflage'])

    def stone_camouflage(self) -> str:
        """Stone Camouflage: The grick has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.ActionsMultiatta..."""
        return "The grick has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.ActionsMultiattack. The grick makes two attacks: one with its tail and one with its tentacles. If it hits with its t"
    def stone_camouflage(self) -> str:
        """Stone Camouflage: The grick has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.ActionsMultiatta..."""
        return "The grick has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.ActionsMultiattack. The grick makes two attacks: one with its tail and one with its tentacles. If it hits with its t"

