# bases1/blue-abishai.py
"""
BlueAbishai creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=blue-abishai
"""
from creature_base import GlobalCreatureBaseClass


class BlueAbishai(GlobalCreatureBaseClass):
    """
    Medium Fiend (Devil creature - BlueAbishai
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 202, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 14, 'CON': 17, 'INT': 22, 'WIS': 23, 'CHAR': 18, 'armor_class': 19, 'alignment': 'Wizard)', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Devil', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['devils_sight', 'multiattack', 'bite', 'lightning_strike', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def devils_sight(self) -> str:
        """Magical darkness doesn't impede the abishai's darkvision.Magic Resistance. The abishai has advantage on saving throws against spells and other magical effects."""
        return "Magical darkness doesn't impede the abishai's darkvision.Magic Resistance. The abishai has advantage on saving throws against spells and other magical effects."

    def multiattack_attack(self) -> str:
        """The abishai makes three Bite or Lightning Strike attacks."""
        return 'The abishai makes three Bite or Lightning Strike attacks.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 13 (2d10 + 2) piercing damage plus 14 (4d6) lightning damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 13 (2d10 + 2) piercing damage plus 14 (4d6) lightning damage.'

    def lightning_strike_attack(self) -> str:
        """Ranged Spell Attack: +12 to hit, range 120 ft., one target. Hit: 36 (8d8) lightning damage."""
        return 'Ranged Spell Attack: +12 to hit, range 120 ft., one target. Hit: 36 (8d8) lightning damage.'

    def spellcasting_attack(self) -> str:
        """The abishai casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 20):"""
        return 'The abishai casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 20):'

