# bases1/hill-giant.py
"""
HillGiant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hill-giant
"""
from creature_base import GlobalCreatureBaseClass


class HillGiant(GlobalCreatureBaseClass):
    """
    HillGiant creature
    Size: Huge, Type: giant, chaotic evil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 105,
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
        "type": "giant, chaotic evil",
        "hit_points_up": [10, 10, 10],
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
        """Multiattack: The giant makes two greatclub attacks.Greatclub. Melee Weapon Attack: +8 to hit, reach 10 ft., one t..."""
        return "The giant makes two greatclub attacks.Greatclub. Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 18 (3d8 + 5) bludgeoning damage.Rock. Ranged Weapon Attack: +8 to hit, range 60/240 ft.,"
    def multiattack(self) -> str:
        """Multiattack: The giant makes two greatclub attacks.Greatclub. Melee Weapon Attack: +8 to hit, reach 10 ft., one t..."""
        return "The giant makes two greatclub attacks.Greatclub. Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 18 (3d8 + 5) bludgeoning damage.Rock. Ranged Weapon Attack: +8 to hit, range 60/240 ft.,"

