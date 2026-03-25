# bases1/black-abishai.py
"""
BlackAbishai creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=black-abishai
"""
from creature_base import GlobalCreatureBaseClass


class BlackAbishai(GlobalCreatureBaseClass):
    """
    Medium Fiend (Devil) creature - BlackAbishai
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 58, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 17, 'CON': 14, 'INT': 13, 'WIS': 16, 'CHAR': 11, 'armor_class': 15, 'alignment': 'typically Lawful Evil Armor Class  15 (natural armor) Hit Points  58 (9d8 + 18) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['devils_sight', 'multiattack', 'bite', 'scimitar', 'creeping_darkness_(recharge_6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def devils_sight(self) -> str:
        """Magical darkness doesn't impede the abishai's darkvision.Magic Resistance. The abishai has advantage on saving throws against spells and other magical effects."""
        return "Magical darkness doesn't impede the abishai's darkvision.Magic Resistance. The abishai has advantage on saving throws against spells and other magical effects."

    def multiattack_attack(self) -> str:
        """The abishai makes one Bite attack and two Scimitar attacks."""
        return 'The abishai makes one Bite attack and two Scimitar attacks.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d10 + 3) piercing damage plus 9 (2d8) acid damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d10 + 3) piercing damage plus 9 (2d8) acid damage.'

    def scimitar_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) force damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) force damage.'

    def creeping_darkness_(recharge_6)_attack(self) -> str:
        """The abishai casts darkness at a point within 120 feet of it, requiring no spell components or concentration. Wisdom is its spellcasting ability for this spell. While the spell persists, the abishai can move the area of darkness up to 60 feet as a bonus action."""
        return 'The abishai casts darkness at a point within 120 feet of it, requiring no spell components or concentration. Wisdom is its spellcasting ability for this spell. While the spell persists, the abishai can move the area of darkness up to 60 feet as a bonus action.'

