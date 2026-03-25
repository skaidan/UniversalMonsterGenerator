# bases1/adult-blue-dracolich.py
"""
AdultBlueDracolich creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=adult-blue-dracolich
"""
from creature_base import GlobalCreatureBaseClass


class AdultBlueDracolich(GlobalCreatureBaseClass):
    """
    Huge undead creature - AdultBlueDracolich
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 225, 'min_level': 1, 'level': 1, 'STR': 25, 'DEX': 10, 'CON': 23, 'INT': 16, 'WIS': 15, 'CHAR': 19, 'armor_class': 19, 'alignment': 'lawful evil Armor Class  19 (natural armor) Hit Points  225 (18d12 + 108) Speed  40 ft.', 'legendary': False, 'size': 'Huge', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['legendary_resistance_(3/day)', 'multiattack', 'bite', 'claw', 'tail', 'frightful_presence', 'lightning_breath_(recharge_5–6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def legendary_resistance_(3/day)(self) -> str:
        """If the dracolich fails a saving throw, it can choose to succeed instead.Magic Resistance. The dracolich has advantage on saving throws against spells and other magical effects."""
        return 'If the dracolich fails a saving throw, it can choose to succeed instead.Magic Resistance. The dracolich has advantage on saving throws against spells and other magical effects.'

    def multiattack_attack(self) -> str:
        """The dracolich can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws."""
        return 'The dracolich can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 18 (2d10 + 7) piercing damage plus 5 (1d10) lightning damage."""
        return 'Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 18 (2d10 + 7) piercing damage plus 5 (1d10) lightning damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +13 to hit, reach 5 ft., one target. Hit: 14 (2d6 + 7) slashing damage."""
        return 'Melee Weapon Attack: +13 to hit, reach 5 ft., one target. Hit: 14 (2d6 + 7) slashing damage.'

    def tail_attack(self) -> str:
        """Melee Weapon Attack: +13 to hit, reach 15 ft., one target. Hit: 16 (2d8 + 7) bludgeoning damage."""
        return 'Melee Weapon Attack: +13 to hit, reach 15 ft., one target. Hit: 16 (2d8 + 7) bludgeoning damage.'

    def frightful_presence_attack(self) -> str:
        """Each creature of the dracolich's choice that is within 120 feet of the dracolich and aware of it must succeed on a DC 18 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dracolich's Frightful Presence for the next 24 hours."""
        return "Each creature of the dracolich's choice that is within 120 feet of the dracolich and aware of it must succeed on a DC 18 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dracolich's Frightful Presence for the next 24 hours."

    def lightning_breath_(recharge_5–6)_attack(self) -> str:
        """The dracolich exhales lightning in a 90-foot line that is 5 feet wide. Each creature in that line must make a DC 20 Dexterity saving throw, taking 66 (12d10) lightning damage on a failed save, or half as much damage on a successful one."""
        return 'The dracolich exhales lightning in a 90-foot line that is 5 feet wide. Each creature in that line must make a DC 20 Dexterity saving throw, taking 66 (12d10) lightning damage on a failed save, or half as much damage on a successful one.'

