# bases1/giant-shark.py
"""
GiantShark creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-shark
"""
from creature_base import GlobalCreatureBaseClass


class GiantShark(GlobalCreatureBaseClass):
    """
    GiantShark creature
    Size: Huge, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 126,
        "min_level": 6,
        "level": 6,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 13,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "beast, unaligned",
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
        self.abilities.extend(['blood_frenzy'])

    def blood_frenzy(self) -> str:
        """Blood Frenzy: The shark has advantage on melee attack rolls against any creature that doesn't have all its hit poi..."""
        return "The shark has advantage on melee attack rolls against any creature that doesn't have all its hit points.Water Breathing. The shark can breathe only underwater.ActionsBite. Melee Weapon Attack: +9 to h"
    def blood_frenzy(self) -> str:
        """Blood Frenzy: The shark has advantage on melee attack rolls against any creature that doesn't have all its hit poi..."""
        return "The shark has advantage on melee attack rolls against any creature that doesn't have all its hit points.Water Breathing. The shark can breathe only underwater.ActionsBite. Melee Weapon Attack: +9 to h"

