# bases1/white-abishai.py
"""
WhiteAbishai creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=white-abishai
"""
from creature_base import GlobalCreatureBaseClass


class WhiteAbishai(GlobalCreatureBaseClass):
    """
    Medium Fiend (Devil) creature - WhiteAbishai
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 68, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 11, 'CON': 18, 'INT': 11, 'WIS': 12, 'CHAR': 13, 'armor_class': 15, 'alignment': 'typically Lawful Evil Armor Class  15 (natural armor) Hit Points  68 (8d8 + 32) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['devils_sight', 'multiattack', 'bite', 'claw', 'longsword']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def devils_sight(self) -> str:
        """Magical darkness doesn't impede the abishai's darkvision.Magic Resistance. The abishai has advantage on saving throws against spells and other magical effects.Reckless. At the start of its turn, the a"""
        return "Magical darkness doesn't impede the abishai's darkvision.Magic Resistance. The abishai has advantage on saving throws against spells and other magical effects.Reckless. At the start of its turn, the a"

    def multiattack_attack(self) -> str:
        """The abishai makes one Bite attack, one Claw attack, and one Longsword attack."""
        return 'The abishai makes one Bite attack, one Claw attack, and one Longsword attack.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) piercing damage plus 3 (1d6) cold damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) piercing damage plus 3 (1d6) cold damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d10 + 3) slashing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d10 + 3) slashing damage.'

    def longsword_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) force damage, or 8 (1d10 + 3) force damage if used with two hands."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) force damage, or 8 (1d10 + 3) force damage if used with two hands.'

