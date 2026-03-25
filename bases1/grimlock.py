# bases1/grimlock.py
"""
Grimlock creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=grimlock
"""
from creature_base import GlobalCreatureBaseClass


class Grimlock(GlobalCreatureBaseClass):
    """
    Medium humanoid (Grimlock) creature - Grimlock
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 11, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 12, 'CON': 12, 'INT': 9, 'WIS': 8, 'CHAR': 6, 'armor_class': 11, 'alignment': 'neutral evil Armor Class  11 Hit Points  11 (2d8 + 2) Speed  30 ft. STR 16 (+3) DEX 12 (+1) CON 12 (+1) INT 9 (-1) WIS 8 (-1) CHA 6 (-2) Skills  Athletics +5', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Grimlock)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['blind_senses', 'spiked_bone_club']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def blind_senses(self) -> str:
        """The grimlock can't use its blindsight while deafened and unable to smell.Keen Hearing and Smell. The grimlock has advantage on Wisdom (Perception) checks that rely on hearing or smell.Stone Camouflage"""
        return "The grimlock can't use its blindsight while deafened and unable to smell.Keen Hearing and Smell. The grimlock has advantage on Wisdom (Perception) checks that rely on hearing or smell.Stone Camouflage"

    def spiked_bone_club_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) bludgeoning damage plus 2 (1d4) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) bludgeoning damage plus 2 (1d4) piercing damage.'

