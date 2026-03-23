# bases1/frost-giant.py
"""
FrostGiant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=frost-giant
"""
from creature_base import GlobalCreatureBaseClass


class FrostGiant(GlobalCreatureBaseClass):
    """
    FrostGiant creature
    Size: Huge, Type: giant, neutral evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 138,
        "min_level": 9,
        "level": 9,
        "STR": 10,
        "DEX": 10,
        "CON": 10,
        "INT": 10,
        "WIS": 10,
        "CHAR": 10,
        "armor_class": 15,
        "alignment": "Unaligned",
        "legendary": False,
        "size": "Huge",
        "type": "giant, neutral evil",
        "hit_points_up": [13, 13, 13],
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
        """Multiattack: The giant makes two greataxe attacks.Greataxe. Melee Weapon Attack: +9 to hit, reach 10 ft., one tar..."""
        return "The giant makes two greataxe attacks.Greataxe. Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 25 (3d12 + 6) slashing damage.Rock. Ranged Weapon Attack: +9 to hit, range 60/240 ft., one"
    def multiattack(self) -> str:
        """Multiattack: The giant makes two greataxe attacks.Greataxe. Melee Weapon Attack: +9 to hit, reach 10 ft., one tar..."""
        return "The giant makes two greataxe attacks.Greataxe. Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 25 (3d12 + 6) slashing damage.Rock. Ranged Weapon Attack: +9 to hit, range 60/240 ft., one"

