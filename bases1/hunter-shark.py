# bases1/hunter-shark.py
"""
HunterShark creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hunter-shark
"""
from creature_base import GlobalCreatureBaseClass


class HunterShark(GlobalCreatureBaseClass):
    """
    HunterShark creature
    Size: Large, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 45,
        "min_level": 3,
        "level": 3,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "beast, unaligned",
        "hit_points_up": [4, 4, 4],
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
        self.abilities.extend(['blood_frenzy'])

    def blood_frenzy(self) -> str:
        """Blood Frenzy: The shark has advantage on melee attack rolls against any creature that doesn't have all its hit poi..."""
        return "The shark has advantage on melee attack rolls against any creature that doesn't have all its hit points.Water Breathing. The shark can breathe only underwater.ActionsBite. Melee Weapon Attack: +6 to h"
    def blood_frenzy(self) -> str:
        """Blood Frenzy: The shark has advantage on melee attack rolls against any creature that doesn't have all its hit poi..."""
        return "The shark has advantage on melee attack rolls against any creature that doesn't have all its hit points.Water Breathing. The shark can breathe only underwater.ActionsBite. Melee Weapon Attack: +6 to h"

