# bases1/giant-scorpion.py
"""
GiantScorpion creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-scorpion
"""
from creature_base import GlobalCreatureBaseClass


class GiantScorpion(GlobalCreatureBaseClass):
    """
    GiantScorpion creature
    Size: Large, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 52,
        "min_level": 4,
        "level": 4,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Large",
        "type": "beast, unaligned",
        "hit_points_up": [5, 5, 5],
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
        """Multiattack: The scorpion makes three attacks: two with its claws and one with its sting.Claw. Melee Weapon Attac..."""
        return "The scorpion makes three attacks: two with its claws and one with its sting.Claw. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) bludgeoning damage, and the target is grappl"
    def multiattack(self) -> str:
        """Multiattack: The scorpion makes three attacks: two with its claws and one with its sting.Claw. Melee Weapon Attac..."""
        return "The scorpion makes three attacks: two with its claws and one with its sting.Claw. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) bludgeoning damage, and the target is grappl"

