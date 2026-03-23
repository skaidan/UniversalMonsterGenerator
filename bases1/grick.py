# bases1/grick.py
"""
Grick creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=grick
"""
from creature_base import GlobalCreatureBaseClass


class Grick(GlobalCreatureBaseClass):
    """
    Grick creature
    Size: Medium, Type: monstrosity, neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 27,
        "min_level": 3,
        "level": 3,
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
        "type": "monstrosity, neutral",
        "hit_points_up": [2, 2, 2],
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
        return "The grick has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.ActionsMultiattack. The grick makes one attack with its tentacles. If that attack hits, the grick can make one beak "
    def stone_camouflage(self) -> str:
        """Stone Camouflage: The grick has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.ActionsMultiatta..."""
        return "The grick has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.ActionsMultiattack. The grick makes one attack with its tentacles. If that attack hits, the grick can make one beak "

