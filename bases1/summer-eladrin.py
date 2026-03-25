# bases1/summer-eladrin.py
"""
SummerEladrin creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=summer-eladrin
"""
from creature_base import GlobalCreatureBaseClass


class SummerEladrin(GlobalCreatureBaseClass):
    """
    Medium Fey (Elf) creature - SummerEladrin
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 165, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 21, 'CON': 16, 'INT': 14, 'WIS': 12, 'CHAR': 18, 'armor_class': 19, 'alignment': 'typically Chaotic Neutral Armor Class  19 (natural armor) Hit Points  165 (22d8 + 66) Speed  50 ft. STR 19 (+4) DEX 21 (+5) CON 16 (+3) INT 14 (+2) WIS 12 (+1) CHA 18 (+4) Skills  Athletics +8', 'legendary': False, 'size': 'Medium', 'type': 'Fey (Elf)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['fearsome_presence', 'multiattack', 'longsword', 'longbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def fearsome_presence(self) -> str:
        """Any non-eladrin creature that starts its turn within 60 feet of the eladrin must make a DC 16 Wisdom saving throw. On a failed save, the creature becomes frightened of the eladrin for 1 minute. A crea"""
        return 'Any non-eladrin creature that starts its turn within 60 feet of the eladrin must make a DC 16 Wisdom saving throw. On a failed save, the creature becomes frightened of the eladrin for 1 minute. A crea'

    def multiattack_attack(self) -> str:
        """The eladrin makes two Longsword or Longbow attacks. The eladrin makes two Longsword or Longbow attacks."""
        return 'The eladrin makes two Longsword or Longbow attacks. The eladrin makes two Longsword or Longbow attacks.'

    def longsword_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) slashing damage, or 15 (2d10 + 4) slashing damage if used with two hands, plus 9 (2d8) fire damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) slashing damage, or 15 (2d10 + 4) slashing damage if used with two hands, plus 9 (2d8) fire damage.'

    def longbow_attack(self) -> str:
        """Ranged Weapon Attack: +9 to hit, range 150/600 ft., one target. Hit: 14 (2d8 + 5) piercing damage plus 9 (2d8) fire damage."""
        return 'Ranged Weapon Attack: +9 to hit, range 150/600 ft., one target. Hit: 14 (2d8 + 5) piercing damage plus 9 (2d8) fire damage.'

