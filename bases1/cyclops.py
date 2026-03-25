# bases1/cyclops.py
"""
Cyclops creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cyclops
"""
from creature_base import GlobalCreatureBaseClass


class Cyclops(GlobalCreatureBaseClass):
    """
    Huge giant creature - Cyclops
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 138, 'min_level': 1, 'level': 1, 'STR': 22, 'DEX': 11, 'CON': 20, 'INT': 8, 'WIS': 6, 'CHAR': 10, 'armor_class': 14, 'alignment': 'chaotic neutral Armor Class  14 (natural armor) Hit Points  138 (12d12 + 60) Speed  30 ft. STR 22 (+6) DEX 11 (+0) CON 20 (+5) INT 8 (-1) WIS 6 (-2) CHA 10 (+0) Senses  passive Perception 8 Languages  Giant Challenge  6 (2300 XP) Poor Depth Perception . The cyclops has disadvantage on any attack roll against a target more than 30 feet away. Actions Multiattack . The cyclops makes two greatclub attacks. Greatclub .  Melee Weapon Attack : +9 to hit', 'legendary': False, 'size': 'Huge', 'type': 'giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['poor_depth_perception', 'multiattack', 'greatclub', 'rock']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def poor_depth_perception(self) -> str:
        """The cyclops has disadvantage on any attack roll against a target more than 30 feet away."""
        return 'The cyclops has disadvantage on any attack roll against a target more than 30 feet away.'

    def multiattack_attack(self) -> str:
        """The cyclops makes two greatclub attacks."""
        return 'The cyclops makes two greatclub attacks.'

    def greatclub_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 19 (3d8 + 6) bludgeoning damage."""
        return 'Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 19 (3d8 + 6) bludgeoning damage.'

    def rock_attack(self) -> str:
        """Ranged Weapon Attack: +9 to hit, range 30/120 ft., one target. Hit: 28 (4d10 + 6) bludgeoning damage."""
        return 'Ranged Weapon Attack: +9 to hit, range 30/120 ft., one target. Hit: 28 (4d10 + 6) bludgeoning damage.'

