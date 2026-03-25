# bases1/awakened-tree.py
"""
AwakenedTree creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=awakened-tree
"""
from creature_base import GlobalCreatureBaseClass


class AwakenedTree(GlobalCreatureBaseClass):
    """
    Huge plant creature - AwakenedTree
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 59, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 6, 'CON': 15, 'INT': 10, 'WIS': 10, 'CHAR': 7, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 (natural armor) Hit Points  59 (7d12 + 14) Speed  20 ft. STR 19 (+4) DEX 6 (-2) CON 15 (+2) INT 10 (+0) WIS 10 (+0) CHA 7 (-2) Damage Vulnerabilities  fire Damage Resistances  bludgeoning', 'legendary': False, 'size': 'Huge', 'type': 'plant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['false_appearance', 'slam']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def false_appearance(self) -> str:
        """While the tree remains motionless, it is indistinguishable from a normal tree."""
        return 'While the tree remains motionless, it is indistinguishable from a normal tree.'

    def slam_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 14 (3d6 + 4) bludgeoning damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 14 (3d6 + 4) bludgeoning damage.'

