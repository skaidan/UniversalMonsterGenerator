# bases1/giant-ape.py
"""
GiantApe creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-ape
"""
from creature_base import GlobalCreatureBaseClass


class GiantApe(GlobalCreatureBaseClass):
    """
    GiantApe creature
    Size: Huge, Type: beast, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 157,
        "min_level": 8,
        "level": 8,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 12,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "beast, unaligned",
        "hit_points_up": [15, 15, 15],
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
        """Multiattack: The ape makes two fist attacks.Fist. Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: ..."""
        return "The ape makes two fist attacks.Fist. Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 22 (3d10 + 6) bludgeoning damage.Rock. Ranged Weapon Attack: +9 to hit, range 50/100 ft., one target"
    def multiattack(self) -> str:
        """Multiattack: The ape makes two fist attacks.Fist. Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: ..."""
        return "The ape makes two fist attacks.Fist. Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 22 (3d10 + 6) bludgeoning damage.Rock. Ranged Weapon Attack: +9 to hit, range 50/100 ft., one target"

