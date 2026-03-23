# bases1/tribal-warrior.py
"""
TribalWarrior creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=tribal-warrior
"""
from creature_base import GlobalCreatureBaseClass


class TribalWarrior(GlobalCreatureBaseClass):
    """
    TribalWarrior creature
    Size: Medium, Type: humanoid (any race), any alignment
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 11,
        "min_level": 2,
        "level": 2,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Medium",
        "type": "humanoid (any race), any alignment",
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
        """Pack Tactics: The warrior has advantage on an attack roll against a creature if at least one of the warrior's alli..."""
        return "The warrior has advantage on an attack roll against a creature if at least one of the warrior's allies is within 5 feet of the creature and the ally isn't incapacitated.ActionsSpear. Melee or Ranged W"
    def pack_tactics(self) -> str:
        """Pack Tactics: The warrior has advantage on an attack roll against a creature if at least one of the warrior's alli..."""
        return "The warrior has advantage on an attack roll against a creature if at least one of the warrior's allies is within 5 feet of the creature and the ally isn't incapacitated.ActionsSpear. Melee or Ranged W"

