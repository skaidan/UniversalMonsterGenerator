# bases1/hyena.py
"""
Hyena creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hyena
"""
from creature_base import GlobalCreatureBaseClass


class Hyena(GlobalCreatureBaseClass):
    """
    Hyena creature
    Size: Medium, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 5,
        "min_level": 1,
        "level": 1,
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
        "type": "beast, unaligned",
        "hit_points_up": [1, 1, 1],
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
        """Pack Tactics: The hyena has advantage on an attack roll against a creature if at least one of the hyena's allies i..."""
        return "The hyena has advantage on an attack roll against a creature if at least one of the hyena's allies is within 5 feet of the creature and the ally isn't incapacitated.ActionsBite. Melee Weapon Attack: +"
    def pack_tactics(self) -> str:
        """Pack Tactics: The hyena has advantage on an attack roll against a creature if at least one of the hyena's allies i..."""
        return "The hyena has advantage on an attack roll against a creature if at least one of the hyena's allies is within 5 feet of the creature and the ally isn't incapacitated.ActionsBite. Melee Weapon Attack: +"

