# bases1/tarrasque.py
"""
Tarrasque creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=tarrasque
"""
from creature_base import GlobalCreatureBaseClass


class Tarrasque(GlobalCreatureBaseClass):
    """
    Gargantuan monstrosity (Titan) creature - Tarrasque
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 676, 'min_level': 1, 'level': 1, 'STR': 30, 'DEX': 11, 'CON': 30, 'INT': 3, 'WIS': 11, 'CHAR': 11, 'armor_class': 25, 'alignment': 'unaligned Armor Class  25 (natural armor) Hit Points  676 (33d20 + 330) Speed  40 ft. STR 30 (+10) DEX 11 (+0) CON 30 (+10) INT 3 (-4) WIS 11 (+0) CHA 11 (+0) Saving Throws  Int +5', 'legendary': False, 'size': 'Gargantuan', 'type': 'monstrosity (Titan)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['legendary_resistance_(3/day)', 'multiattack', 'bite', 'claw', 'horns', 'tail', 'frightful_presence', 'swallow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def legendary_resistance_(3/day)(self) -> str:
        """If the tarrasque fails a saving throw, it can choose to succeed instead.Magic Resistance. The tarrasque has advantage on saving throws against spells and other magical effects.Reflective Carapace. Any"""
        return 'If the tarrasque fails a saving throw, it can choose to succeed instead.Magic Resistance. The tarrasque has advantage on saving throws against spells and other magical effects.Reflective Carapace. Any'

    def multiattack_attack(self) -> str:
        """The tarrasque can use its Frightful Presence. It then makes five attacks: one with its bite, two with its claws, one with its horns, and one with its tail. It can use its Swallow instead of its bite."""
        return 'The tarrasque can use its Frightful Presence. It then makes five attacks: one with its bite, two with its claws, one with its horns, and one with its tail. It can use its Swallow instead of its bite.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +19 to hit, reach 10 ft., one target. Hit: 36 (4d12 + 10) piercing damage. If the target is a creature, it is grappled (escape DC 20). Until this grapple ends, the target is restrained, and the tarrasque can't bite another target."""
        return "Melee Weapon Attack: +19 to hit, reach 10 ft., one target. Hit: 36 (4d12 + 10) piercing damage. If the target is a creature, it is grappled (escape DC 20). Until this grapple ends, the target is restrained, and the tarrasque can't bite another target."

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +19 to hit, reach 15 ft., one target. Hit: 28 (4d8 + 10) stashing damage."""
        return 'Melee Weapon Attack: +19 to hit, reach 15 ft., one target. Hit: 28 (4d8 + 10) stashing damage.'

    def horns_attack(self) -> str:
        """Melee Weapon Attack: +19 to hit, reach 10 ft., one target. Hit: 32 (4d10 + 10) piercing damage."""
        return 'Melee Weapon Attack: +19 to hit, reach 10 ft., one target. Hit: 32 (4d10 + 10) piercing damage.'

    def tail_attack(self) -> str:
        """Melee Weapon Attack: +19 to hit, reach 20 ft., one target. Hit: 24 (4d6 + 10) bludgeoning damage. If the target is a creature, it must succeed on a DC 20 Strength saving throw or be knocked prone."""
        return 'Melee Weapon Attack: +19 to hit, reach 20 ft., one target. Hit: 24 (4d6 + 10) bludgeoning damage. If the target is a creature, it must succeed on a DC 20 Strength saving throw or be knocked prone.'

    def frightful_presence_attack(self) -> str:
        """Each creature of the tarrasque's choice within 120 feet of it and aware of it must succeed on a DC 17 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, with disadvantage if the tarrasque is within line of sight, ending the effect on itself on a success. If a creature's saving throw Is successful or the effect ends for it, the creature is immune to the tarrasque's Frightful Presence for the next 24 hours."""
        return "Each creature of the tarrasque's choice within 120 feet of it and aware of it must succeed on a DC 17 Wisdom saving throw or become frightened for 1 minute. A creature can repeat the saving throw at the end of each of its turns, with disadvantage if the tarrasque is within line of sight, ending the effect on itself on a success. If a creature's saving throw Is successful or the effect ends for it, the creature is immune to the tarrasque's Frightful Presence for the next 24 hours."

    def swallow_attack(self) -> str:
        """The tarrasque makes one bite attack against a Large or smaller creature it is grappling. If the attack hits, the target takes the bite's damage, the target is swallowed, and the grapple ends. While swallowed, the creature is blinded and restrained, it has total cover against attacks and other effects outside the tarrasque, and it takes bO (I6d6) acid damage at the start of each of the tarrasque's turns. If the tarrasque takes 60 damage or more on a single turn from a creature inside it, the tarrasque must succeed on a DC 30 Constitution saving throw at the end of that turn or regurgitate all swallowed creatures, which fall prone in a space within 10 feet of the tarrasque. If the tarrasque dies, a swallowed creature is no longer restrained by it and can escape from the corpse by using 30 feet of movement, exiting prone."""
        return "The tarrasque makes one bite attack against a Large or smaller creature it is grappling. If the attack hits, the target takes the bite's damage, the target is swallowed, and the grapple ends. While swallowed, the creature is blinded and restrained, it has total cover against attacks and other effects outside the tarrasque, and it takes bO (I6d6) acid damage at the start of each of the tarrasque's turns. If the tarrasque takes 60 damage or more on a single turn from a creature inside it, the tarrasque must succeed on a DC 30 Constitution saving throw at the end of that turn or regurgitate all swallowed creatures, which fall prone in a space within 10 feet of the tarrasque. If the tarrasque dies, a swallowed creature is no longer restrained by it and can escape from the corpse by using 30 feet of movement, exiting prone."

