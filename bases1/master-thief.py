# bases1/master-thief.py
"""
MasterThief creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=master-thief
"""
from creature_base import GlobalCreatureBaseClass


class MasterThief(GlobalCreatureBaseClass):
    """
    Medium Humanoid creature - MasterThief
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 84, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 18, 'CON': 14, 'INT': 11, 'WIS': 11, 'CHAR': 12, 'armor_class': 16, 'alignment': 'any alignment Armor Class  16 (studded leather) Hit Points  84 (13d8 + 26) Speed  30 ft. STR 11 (+0) DEX 18 (+4) CON 14 (+2) INT 11 (+0) WIS 11 (+0) CHA 12 (+1) Saving Throws  Dex +7', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['evasion', 'multiattack', 'shortsword', 'shortbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def evasion(self) -> str:
        """If the thief is subjected to an effect that allows it to make a Dexterity saving throw to take only half damage, the thief instead takes no damage if it succeeds on the saving throw and only half dama"""
        return 'If the thief is subjected to an effect that allows it to make a Dexterity saving throw to take only half damage, the thief instead takes no damage if it succeeds on the saving throw and only half dama'

    def multiattack_attack(self) -> str:
        """The thief makes three Shortsword or Shortbow attacks."""
        return 'The thief makes three Shortsword or Shortbow attacks.'

    def shortsword_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) piercing damage plus 3 (1d6) poison damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) piercing damage plus 3 (1d6) poison damage.'

    def shortbow_attack(self) -> str:
        """Ranged Weapon Attack: +7 to hit, range 80/320 ft., one target. Hit: 7 (1d6 + 4) piercing damage plus 3 (1d6) poison damage."""
        return 'Ranged Weapon Attack: +7 to hit, range 80/320 ft., one target. Hit: 7 (1d6 + 4) piercing damage plus 3 (1d6) poison damage.'

