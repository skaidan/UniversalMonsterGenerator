# bases1/thug.py
"""
Thug creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=thug
"""
from creature_base import GlobalCreatureBaseClass


class Thug(GlobalCreatureBaseClass):
    """
    Thug creature
    Size: Medium, Type: humanoid (any race), any non-good alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 32,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 11,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (any race), any non-good alignment",
        "hit_points_up": [3, 3, 3],
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
        self.abilities.extend(['pack_tactics'])

    def pack_tactics(self) -> str:
        """Pack Tactics: The thug has advantage on an attack roll against a creature if at least one of the thug's allies is ..."""
        return "The thug has advantage on an attack roll against a creature if at least one of the thug's allies is within 5 feet of the creature and the ally isn't incapacitated.ActionsMultiattack. The thug makes tw"
    def pack_tactics(self) -> str:
        """Pack Tactics: The thug has advantage on an attack roll against a creature if at least one of the thug's allies is ..."""
        return "The thug has advantage on an attack roll against a creature if at least one of the thug's allies is within 5 feet of the creature and the ally isn't incapacitated.ActionsMultiattack. The thug makes tw"

