# bases1/scout.py
"""
Scout creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=scout
"""
from creature_base import GlobalCreatureBaseClass


class Scout(GlobalCreatureBaseClass):
    """
    Medium humanoid (any race) creature - Scout
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 16, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 14, 'CON': 12, 'INT': 11, 'WIS': 13, 'CHAR': 11, 'armor_class': 13, 'alignment': 'any alignment Armor Class  13 (leather armor) Hit Points  16 (3d8 + 3) Speed  30 ft. STR 11 (+0) DEX 14 (+2) CON 12 (+1) INT 11 (+0) WIS 13 (+1) CHA 11 (+0) Skills  Nature +4', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (any race)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_hearing_and_sight', 'multiattack', 'shortsword', 'longbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_hearing_and_sight(self) -> str:
        """The scout has advantage on Wisdom (Perception) checks that rely on hearing or sight."""
        return 'The scout has advantage on Wisdom (Perception) checks that rely on hearing or sight.'

    def multiattack_attack(self) -> str:
        """The scout makes two melee attacks or two ranged attacks."""
        return 'The scout makes two melee attacks or two ranged attacks.'

    def shortsword_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.'

    def longbow_attack(self) -> str:
        """Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage."""
        return 'Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage.'

