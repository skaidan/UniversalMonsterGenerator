# bases1/bodak.py
"""
Bodak creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bodak
"""
from creature_base import GlobalCreatureBaseClass


class Bodak(GlobalCreatureBaseClass):
    """
    Medium Undead creature - Bodak
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 58, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 16, 'CON': 15, 'INT': 7, 'WIS': 12, 'CHAR': 12, 'armor_class': 15, 'alignment': 'typically Chaotic Evil Armor Class  15 (natural armor) Hit Points  58 (9d8 + 18) Speed  30 ft. STR 15 (+2) DEX 16 (+3) CON 15 (+2) INT 7 (-2) WIS 12 (+1) CHA 12 (+1) Skills  Perception +4', 'legendary': False, 'size': 'Medium', 'type': 'Undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['death_gaze', 'fist', 'withering_gaze']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def death_gaze(self) -> str:
        """When a creature that can see the bodak's eyes starts its turn within 30 feet of the bodak, the bodak can force it to make a DC 13 Constitution saving throw if the bodak isn't incapacitated and can see"""
        return "When a creature that can see the bodak's eyes starts its turn within 30 feet of the bodak, the bodak can force it to make a DC 13 Constitution saving throw if the bodak isn't incapacitated and can see"

    def fist_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) bludgeoning damage plus 9 (2d8) necrotic damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) bludgeoning damage plus 9 (2d8) necrotic damage.'

    def withering_gaze_attack(self) -> str:
        """One creature that the bodak can see within 60 feet of it must make a DC 13 Constitution saving throw, taking 22 (4d10) necrotic damage on a failed save, or half as much damage on a successful one."""
        return 'One creature that the bodak can see within 60 feet of it must make a DC 13 Constitution saving throw, taking 22 (4d10) necrotic damage on a failed save, or half as much damage on a successful one.'

