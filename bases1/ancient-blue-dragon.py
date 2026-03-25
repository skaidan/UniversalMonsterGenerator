# bases1/ancient-blue-dragon.py
"""
AncientBlueDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ancient-blue-dragon
"""
from creature_base import GlobalCreatureBaseClass


class AncientBlueDragon(GlobalCreatureBaseClass):
    """
    Gargantuan dragon (Chromatic) creature - AncientBlueDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 481, 'min_level': 1, 'level': 1, 'STR': 29, 'DEX': 10, 'CON': 27, 'INT': 18, 'WIS': 17, 'CHAR': 21, 'armor_class': 22, 'alignment': 'lawful evil Armor Class  22 (natural armor) Hit Points  481 (26d20 + 208) Speed  40 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'dragon (Chromatic)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['legendary_resistance_(3/day)', 'multiattack', 'bite', 'claw', 'tail', 'frightful_presence', 'lightning_breath_(recharge_5-6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def legendary_resistance_(3/day)(self) -> str:
        """If the dragon fails a saving throw, it can choose to succeed instead."""
        return 'If the dragon fails a saving throw, it can choose to succeed instead.'

    def multiattack_attack(self) -> str:
        """The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws."""
        return 'The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +16 to hit, reach 15 ft., one target. Hit: 20 (2d10 + 9) piercing damage plus 11 (2d10) lightning damage."""
        return 'Melee Weapon Attack: +16 to hit, reach 15 ft., one target. Hit: 20 (2d10 + 9) piercing damage plus 11 (2d10) lightning damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +16 to hit, reach 10 ft., one target. Hit: 16 (2d6 + 9) slashing damage."""
        return 'Melee Weapon Attack: +16 to hit, reach 10 ft., one target. Hit: 16 (2d6 + 9) slashing damage.'

    def tail_attack(self) -> str:
        """Melee Weapon Attack: +16 to hit, reach 20 ft., one target. Hit: 18 (2d8 + 9) bludgeoning damage."""
        return 'Melee Weapon Attack: +16 to hit, reach 20 ft., one target. Hit: 18 (2d8 + 9) bludgeoning damage.'

    def frightful_presence_attack(self) -> str:
        """Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 20 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours."""
        return "Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 20 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours."

    def lightning_breath_(recharge_5-6)_attack(self) -> str:
        """The dragon exhales lightning in a 120-foot line that is 10 feet wide. Each creature in that line must make a DC 23 Dexterity saving throw, taking 88 (16d10) lightning damage on a failed save, or half as much damage on a successful one."""
        return 'The dragon exhales lightning in a 120-foot line that is 10 feet wide. Each creature in that line must make a DC 23 Dexterity saving throw, taking 88 (16d10) lightning damage on a failed save, or half as much damage on a successful one.'

