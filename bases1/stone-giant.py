# bases1/stone-giant.py
"""
StoneGiant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=stone-giant
"""
from creature_base import GlobalCreatureBaseClass


class StoneGiant(GlobalCreatureBaseClass):
    """
    StoneGiant creature
    Size: Huge, Type: giant, neutral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 126,
        "min_level": 8,
        "level": 8,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 17,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "giant, neutral",
        "hit_points_up": [12, 12, 12],
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
        """Stone Camouflage: The giant has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.ActionsMultiatta..."""
        return "The giant has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.ActionsMultiattack. The giant makes two greatclub attacks.Greatclub. Melee Weapon Attack: +9 to hit, reach 15 ft., o"
    def stone_camouflage(self) -> str:
        """Stone Camouflage: The giant has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.ActionsMultiatta..."""
        return "The giant has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.ActionsMultiattack. The giant makes two greatclub attacks.Greatclub. Melee Weapon Attack: +9 to hit, reach 15 ft., o"

