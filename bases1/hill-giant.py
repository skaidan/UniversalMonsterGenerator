# bases1/hill-giant.py
"""
HillGiant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hill-giant
"""
from creature_base import GlobalCreatureBaseClass


class HillGiant(GlobalCreatureBaseClass):
    """
    Huge giant creature - HillGiant
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 105, 'min_level': 1, 'level': 1, 'STR': 21, 'DEX': 8, 'CON': 19, 'INT': 5, 'WIS': 9, 'CHAR': 6, 'armor_class': 13, 'alignment': 'chaotic evil Armor Class  13 (natural armor) Hit Points  105 (10d12 + 40) Speed  40 ft. STR 21 (+5) DEX 8 (-1) CON 19 (+4) INT 5 (-3) WIS 9 (-1) CHA 6 (-2) Skills  Perception +2 Senses  passive Perception 12 Languages  Giant Challenge  5 (1800 XP) Actions Multiattack . The giant makes two greatclub attacks. Greatclub .  Melee Weapon Attack : +8 to hit', 'legendary': False, 'size': 'Huge', 'type': 'giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'greatclub', 'rock']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The giant makes two greatclub attacks."""
        return 'The giant makes two greatclub attacks.'

    def greatclub_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 18 (3d8 + 5) bludgeoning damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 18 (3d8 + 5) bludgeoning damage.'

    def rock_attack(self) -> str:
        """Ranged Weapon Attack: +8 to hit, range 60/240 ft., one target. Hit: 21 (3d10 + 5) bludgeoning damage."""
        return 'Ranged Weapon Attack: +8 to hit, range 60/240 ft., one target. Hit: 21 (3d10 + 5) bludgeoning damage.'

