# bases1/awakened-tree.py
"""
AwakenedTree creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=awakened-tree
"""
from creature_base import GlobalCreatureBaseClass


class AwakenedTree(GlobalCreatureBaseClass):
    """
    AwakenedTree creature
    Size: Huge, Type: plant, unaligned
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {
        "hit_points": 59,
        "min_level": 3,
        "level": 3,
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
        "type": "plant, unaligned",
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
        self.abilities.extend(['false_appearance'])

    def false_appearance(self) -> str:
        """False Appearance: While the tree remains motionless, it is indistinguishable from a normal tree.ActionsSlam. Melee Wea..."""
        return "While the tree remains motionless, it is indistinguishable from a normal tree.ActionsSlam. Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 14 (3d6 + 4) bludgeoning damage.An awakened tr"
    def false_appearance(self) -> str:
        """False Appearance: While the tree remains motionless, it is indistinguishable from a normal tree.ActionsSlam. Melee Wea..."""
        return "While the tree remains motionless, it is indistinguishable from a normal tree.ActionsSlam. Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 14 (3d6 + 4) bludgeoning damage.An awakened tr"

