# bases1/bone-devil.py
"""
BoneDevil creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bone-devil
"""
from creature_base import GlobalCreatureBaseClass


class BoneDevil(GlobalCreatureBaseClass):
    """
    Large fiend (Devil) creature - BoneDevil
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 142, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 16, 'CON': 18, 'INT': 13, 'WIS': 14, 'CHAR': 16, 'armor_class': 19, 'alignment': 'lawful evil Armor Class  19 (natural armor) Hit Points  142 (15d10 + 60) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['devils_sight', 'multiattack', 'claw', 'sting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def devils_sight(self) -> str:
        """Magical darkness doesn't impede the devil's darkvision.Magic Resistance. The devil has advantage on saving throws against spells and other magical effects."""
        return "Magical darkness doesn't impede the devil's darkvision.Magic Resistance. The devil has advantage on saving throws against spells and other magical effects."

    def multiattack_attack(self) -> str:
        """The devil makes three attacks: two with its claws and one with its sting."""
        return 'The devil makes three attacks: two with its claws and one with its sting.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 8 (1d8 + 4) slashing damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 8 (1d8 + 4) slashing damage.'

    def sting_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 13 (2d8 + 4) piercing damage plus 17 (5d6) poison damage, and the target must succeed on a DC 14 Constitution saving throw or become poisoned for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 13 (2d8 + 4) piercing damage plus 17 (5d6) poison damage, and the target must succeed on a DC 14 Constitution saving throw or become poisoned for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

