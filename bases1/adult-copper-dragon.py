# bases1/adult-copper-dragon.py
"""
AdultCopperDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=adult-copper-dragon
"""
from creature_base import GlobalCreatureBaseClass


class AdultCopperDragon(GlobalCreatureBaseClass):
    """
    Huge dragon (Metallic) creature - AdultCopperDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 184, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 12, 'CON': 21, 'INT': 18, 'WIS': 15, 'CHAR': 17, 'armor_class': 18, 'alignment': 'chaotic good Armor Class  18 (natural armor) Hit Points  184 (16d12 + 80) Speed  40 ft.', 'legendary': False, 'size': 'Huge', 'type': 'dragon (Metallic)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['legendary_resistance_(3/day)', 'multiattack', 'bite', 'claw', 'tail', 'frightful_presence', 'breath_weapons_(recharge_5-6)', 'acid_breath', 'slowing_breath']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def legendary_resistance_(3/day)(self) -> str:
        """If the dragon fails a saving throw, it can choose to succeed instead."""
        return 'If the dragon fails a saving throw, it can choose to succeed instead.'

    def multiattack_attack(self) -> str:
        """The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws."""
        return 'The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +11 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage."""
        return 'Melee Weapon Attack: +11 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage."""
        return 'Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage.'

    def tail_attack(self) -> str:
        """Melee Weapon Attack: +11 to hit, reach 15 ft., one target. Hit: 15 (2d8 + 6) bludgeoning damage."""
        return 'Melee Weapon Attack: +11 to hit, reach 15 ft., one target. Hit: 15 (2d8 + 6) bludgeoning damage.'

    def frightful_presence_attack(self) -> str:
        """Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 16 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours."""
        return "Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 16 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours."

    def breath_weapons_(recharge_5-6)_attack(self) -> str:
        """The dragon uses one of the following breath weapons."""
        return 'The dragon uses one of the following breath weapons.'

    def acid_breath_attack(self) -> str:
        """The dragon exhales acid in an 60-foot line that is 5 feet wide. Each creature in that line must make a DC 18 Dexterity saving throw, taking 54 (12d8) acid damage on a failed save, or half as much damage on a successful one."""
        return 'The dragon exhales acid in an 60-foot line that is 5 feet wide. Each creature in that line must make a DC 18 Dexterity saving throw, taking 54 (12d8) acid damage on a failed save, or half as much damage on a successful one.'

    def slowing_breath_attack(self) -> str:
        """The dragon exhales gas in a 60-foot cone. Each creature in that area must succeed on a DC 18 Constitution saving throw. On a failed save, the creature can't use reactions, its speed is halved, and it can't make more than one attack on its turn. In addition, the creature can use either an action or a bonus action on its turn, but not both. These effects last for 1 minute. The creature can repeat the saving throw at the end of each of its turns, ending the effect on itself with a successful save."""
        return "The dragon exhales gas in a 60-foot cone. Each creature in that area must succeed on a DC 18 Constitution saving throw. On a failed save, the creature can't use reactions, its speed is halved, and it can't make more than one attack on its turn. In addition, the creature can use either an action or a bonus action on its turn, but not both. These effects last for 1 minute. The creature can repeat the saving throw at the end of each of its turns, ending the effect on itself with a successful save."

