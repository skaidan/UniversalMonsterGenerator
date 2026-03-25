# bases1/adult-green-dragon.py
"""
AdultGreenDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=adult-green-dragon
"""
from creature_base import GlobalCreatureBaseClass


class AdultGreenDragon(GlobalCreatureBaseClass):
    """
    Huge dragon (Chromatic) creature - AdultGreenDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 207, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 12, 'CON': 21, 'INT': 18, 'WIS': 15, 'CHAR': 17, 'armor_class': 19, 'alignment': 'lawful evil Armor Class  19 (natural armor) Hit Points  207 (18d12 + 90) Speed  40 ft.', 'legendary': False, 'size': 'Huge', 'type': 'dragon (Chromatic)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['amphibious', 'multiattack', 'bite', 'claw', 'tail', 'frightful_presence', 'poison_breath_(recharge_5-6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def amphibious(self) -> str:
        """The dragon can breathe air and water.Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead."""
        return 'The dragon can breathe air and water.Legendary Resistance (3/Day). If the dragon fails a saving throw, it can choose to succeed instead.'

    def multiattack_attack(self) -> str:
        """The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws."""
        return 'The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +11 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage plus 7 (2d6) poison damage."""
        return 'Melee Weapon Attack: +11 to hit, reach 10 ft., one target. Hit: 17 (2d10 + 6) piercing damage plus 7 (2d6) poison damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage."""
        return 'Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 13 (2d6 + 6) slashing damage.'

    def tail_attack(self) -> str:
        """Melee Weapon Attack: +11 to hit, reach 15 ft., one target. Hit: 15 (2d8 + 6) bludgeoning damage."""
        return 'Melee Weapon Attack: +11 to hit, reach 15 ft., one target. Hit: 15 (2d8 + 6) bludgeoning damage.'

    def frightful_presence_attack(self) -> str:
        """Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 16 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours."""
        return "Each creature of the dragon's choice that is within 120 feet of the dragon and aware of it must succeed on a DC 16 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dragon's Frightful Presence for the next 24 hours."

    def poison_breath_(recharge_5-6)_attack(self) -> str:
        """The dragon exhales poisonous gas in a 60-foot cone. Each creature in that area must make a DC 18 Constitution saving throw, taking 56 (16d6) poison damage on a failed save, or half as much damage on a successful one."""
        return 'The dragon exhales poisonous gas in a 60-foot cone. Each creature in that area must make a DC 18 Constitution saving throw, taking 56 (16d6) poison damage on a failed save, or half as much damage on a successful one.'

