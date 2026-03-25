# bases1/ancient-copper-dragon.py
"""
AncientCopperDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ancient-copper-dragon
"""
from creature_base import GlobalCreatureBaseClass


class AncientCopperDragon(GlobalCreatureBaseClass):
    """
    Gargantuan dragon (Metallic) creature - AncientCopperDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 350, 'min_level': 1, 'level': 1, 'STR': 27, 'DEX': 12, 'CON': 25, 'INT': 20, 'WIS': 17, 'CHAR': 19, 'armor_class': 21, 'alignment': 'chaotic good Armor Class  21 (natural armor) Hit Points  350 (20d20 + 140) Speed  40 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'dragon (Metallic)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['legendary_resistance_(3/day)', 'multiattack', 'bite', 'claw', 'tail', 'frightful_presence', 'breath_weapons_(recharge_5-6)', 'acid_breath', 'slowing_breath', 'change_shape']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def legendary_resistance_(3/day)(self) -> str:
        """If the dragon fails a saving throw, it can choose to succeed instead."""
        return 'If the dragon fails a saving throw, it can choose to succeed instead.'

    def multiattack_attack(self) -> str:
        """The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws."""
        return 'The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +15 to hit, reach 15 ft., one target. Hit: 19 (2d10 + 8) piercing damage."""
        return 'Melee Weapon Attack: +15 to hit, reach 15 ft., one target. Hit: 19 (2d10 + 8) piercing damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +15 to hit, reach 10 ft., one target. Hit: 15 (2d6 + 8) slashing damage."""
        return 'Melee Weapon Attack: +15 to hit, reach 10 ft., one target. Hit: 15 (2d6 + 8) slashing damage.'

    def tail_attack(self) -> str:
        """Melee Weapon Attack: +15 to hit, reach 20 ft., one target. Hit: 17 (2d8 + 8) bludgeoning damage."""
        return 'Melee Weapon Attack: +15 to hit, reach 20 ft., one target. Hit: 17 (2d8 + 8) bludgeoning damage.'

    def frightful_presence_attack(self) -> str:
        """Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 19 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours."""
        return "Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 19 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours."

    def breath_weapons_(recharge_5-6)_attack(self) -> str:
        """The dragon uses one of the following breath weapons."""
        return 'The dragon uses one of the following breath weapons.'

    def acid_breath_attack(self) -> str:
        """The dragon exhales acid in an 90-foot line that is 10 feet wide. Each creature in that line must make a DC 22 Dexterity saving throw, taking 63 (14d8) acid damage on a failed save, or half as much damage on a successful one."""
        return 'The dragon exhales acid in an 90-foot line that is 10 feet wide. Each creature in that line must make a DC 22 Dexterity saving throw, taking 63 (14d8) acid damage on a failed save, or half as much damage on a successful one.'

    def slowing_breath_attack(self) -> str:
        """The dragon exhales gas in a 90-foot cone. Each creature in that area must succeed on a DC 22 Constitution saving throw. On a failed save, the creature can't use reactions, its speed is halved, and it can't make more than one attack on its turn. In addition, the creature can use either an action or a bonus action on its turn, but not both. These effects last for 1 minute. The creature can repeat the saving throw at the end of each of its turns, ending the effect on itself with a successful save."""
        return "The dragon exhales gas in a 90-foot cone. Each creature in that area must succeed on a DC 22 Constitution saving throw. On a failed save, the creature can't use reactions, its speed is halved, and it can't make more than one attack on its turn. In addition, the creature can use either an action or a bonus action on its turn, but not both. These effects last for 1 minute. The creature can repeat the saving throw at the end of each of its turns, ending the effect on itself with a successful save."

    def change_shape_attack(self) -> str:
        """The dragon magically polymorphs into a humanoid or beast that has a challenge rating no higher than its own, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the dragon's choice). In a new form, the dragon retains its alignment, hit points, Hit Dice, ability to speak, proficiencies, Legendary Resistance, lair actions, and Intelligence, Wisdom, and Charisma scores, as well as this action. Its statistics and capabilities are otherwise replaced by those of the new form, except any class features or legendary actions of that form."""
        return "The dragon magically polymorphs into a humanoid or beast that has a challenge rating no higher than its own, or back into its true form. It reverts to its true form if it dies. Any equipment it is wearing or carrying is absorbed or borne by the new form (the dragon's choice). In a new form, the dragon retains its alignment, hit points, Hit Dice, ability to speak, proficiencies, Legendary Resistance, lair actions, and Intelligence, Wisdom, and Charisma scores, as well as this action. Its statistics and capabilities are otherwise replaced by those of the new form, except any class features or legendary actions of that form."

