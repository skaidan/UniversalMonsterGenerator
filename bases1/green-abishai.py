# bases1/green-abishai.py
"""
GreenAbishai creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=green-abishai
"""
from creature_base import GlobalCreatureBaseClass


class GreenAbishai(GlobalCreatureBaseClass):
    """
    Medium Fiend (Devil) creature - GreenAbishai
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 195, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 17, 'CON': 16, 'INT': 17, 'WIS': 12, 'CHAR': 19, 'armor_class': 18, 'alignment': 'typically Lawful Evil Armor Class  18 (natural armor) Hit Points  195 (26d8 + 78) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['devils_sight', 'multiattack', 'fiendish_claw', 'spellcasting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def devils_sight(self) -> str:
        """Magical darkness doesn't impede the abishai's darkvision.Magic Resistance. The abishai has advantage on saving throws against spells and other magical effects."""
        return "Magical darkness doesn't impede the abishai's darkvision.Magic Resistance. The abishai has advantage on saving throws against spells and other magical effects."

    def multiattack_attack(self) -> str:
        """The abishai makes two Fiendish Claw attacks, or it makes one Fiendish Claw attack and uses Spellcasting."""
        return 'The abishai makes two Fiendish Claw attacks, or it makes one Fiendish Claw attack and uses Spellcasting.'

    def fiendish_claw_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 12 (2d8 + 3) force damage. If the target is a creature, it must succeed on a DC 16 Constitution saving throw or take 16 (3d10) poison damage and become poisoned for 1 minute. The poisoned target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 12 (2d8 + 3) force damage. If the target is a creature, it must succeed on a DC 16 Constitution saving throw or take 16 (3d10) poison damage and become poisoned for 1 minute. The poisoned target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

    def spellcasting_attack(self) -> str:
        """The abishai casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 17):"""
        return 'The abishai casts one of the following spells, requiring no material components and using Charisma as the spellcasting ability (spell save DC 17):'

