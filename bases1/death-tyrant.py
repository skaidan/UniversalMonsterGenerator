# bases1/death-tyrant.py
"""
DeathTyrant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=death-tyrant
"""
from creature_base import GlobalCreatureBaseClass


class DeathTyrant(GlobalCreatureBaseClass):
    """
    Large undead creature - DeathTyrant
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 187, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 14, 'CON': 14, 'INT': 19, 'WIS': 15, 'CHAR': 19, 'armor_class': 19, 'alignment': 'lawful evil Armor Class  19 (natural armor) Hit Points  187 (25d10 + 50) Speed  0 ft.', 'legendary': False, 'size': 'Large', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['negative_energy_cone', 'bite', 'eye_rays', 'ability_1__charm_ray', 'ability_2__paralyzing_ray', 'ability_3__fear_ray', 'ability_4__slowing_ray', 'ability_5__enervation_ray', 'ability_6__telekinetic_ray', 'ability_7__sleep_ray', 'ability_8__petrification_ray', 'ability_9__disintegration_ray', 'ability_10__death_ray']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def negative_energy_cone(self) -> str:
        """The death tyrant's central eye emits an invisible, magical 1 50-foot cone of negative energy. At the start of each of its turns, the tyrant decides which way the cone faces and whether the cone is act"""
        return "The death tyrant's central eye emits an invisible, magical 1 50-foot cone of negative energy. At the start of each of its turns, the tyrant decides which way the cone faces and whether the cone is act"

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 14 (4d6) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 14 (4d6) piercing damage.'

    def eye_rays_attack(self) -> str:
        """The death tyrant shoots three of the following magical eye rays at random (reroll duplicates), choosing one to three targets it can see within 120 feet of it:"""
        return 'The death tyrant shoots three of the following magical eye rays at random (reroll duplicates), choosing one to three targets it can see within 120 feet of it:'

    def attack_1_charm_ray_attack(self) -> str:
        """The targeted creature must succeed on a DC 17 Wisdom saving throw or be charmed by the tyrant for 1 hour, or until the beholder harms the creature."""
        return 'The targeted creature must succeed on a DC 17 Wisdom saving throw or be charmed by the tyrant for 1 hour, or until the beholder harms the creature.'

    def attack_2_paralyzing_ray_attack(self) -> str:
        """The targeted creature must succeed on a DC 17 Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'The targeted creature must succeed on a DC 17 Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

    def attack_3_fear_ray_attack(self) -> str:
        """The targeted creature must succeed on a DC 17 Wisdom saving throw or be frightened for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'The targeted creature must succeed on a DC 17 Wisdom saving throw or be frightened for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

    def attack_4_slowing_ray_attack(self) -> str:
        """The targeted creature must succeed on a DC 17 Dexterity saving throw. On a failed save, the target's speed is halved for 1 minute. In addition, the creature can't take reactions, and it can take either an action or a bonus action on its turn, not both. The creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return "The targeted creature must succeed on a DC 17 Dexterity saving throw. On a failed save, the target's speed is halved for 1 minute. In addition, the creature can't take reactions, and it can take either an action or a bonus action on its turn, not both. The creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."

    def attack_5_enervation_ray_attack(self) -> str:
        """The targeted creature must make a DC 17 Constitution saving throw, taking 36 (8d8) necrotic damage on a failed save, or half as much damage on a successful one."""
        return 'The targeted creature must make a DC 17 Constitution saving throw, taking 36 (8d8) necrotic damage on a failed save, or half as much damage on a successful one.'

    def attack_6_telekinetic_ray_attack(self) -> str:
        """If the target is a creature, it must succeed on a DC 17 Strength saving throw or the tyrant moves it up to 30 feet in any direction. The target is restrained by the ray's telekinetic grip until the start of the tyrant's next turn or until the tyrant is incapacitated. If the target is an object weighing 300 pounds or less that isn't being worn or carried, it is moved up to 30 feet in any direction. The tyrant can also exert fine control on objects with this ray, such as manipulating a simple tool or opening a door or a container."""
        return "If the target is a creature, it must succeed on a DC 17 Strength saving throw or the tyrant moves it up to 30 feet in any direction. The target is restrained by the ray's telekinetic grip until the start of the tyrant's next turn or until the tyrant is incapacitated. If the target is an object weighing 300 pounds or less that isn't being worn or carried, it is moved up to 30 feet in any direction. The tyrant can also exert fine control on objects with this ray, such as manipulating a simple tool or opening a door or a container."

    def attack_7_sleep_ray_attack(self) -> str:
        """The targeted creature must succeed on a DC 17 Wisdom saving throw or fall asleep and remain unconscious for 1 minute. The target awakens if it takes damage or another creature takes an action to wake it. This ray has no effect on constructs and undead."""
        return 'The targeted creature must succeed on a DC 17 Wisdom saving throw or fall asleep and remain unconscious for 1 minute. The target awakens if it takes damage or another creature takes an action to wake it. This ray has no effect on constructs and undead.'

    def attack_8_petrification_ray_attack(self) -> str:
        """The targeted creature must make a DC 17 Dexterity saving throw. On a failed save, the creature begins to turn to stone and is restrained. It must repeat the saving throw at the end of its next turn. On a success, the effect ends. On a failure, the creature is petrified until freed by the greater restoration spell or other magic."""
        return 'The targeted creature must make a DC 17 Dexterity saving throw. On a failed save, the creature begins to turn to stone and is restrained. It must repeat the saving throw at the end of its next turn. On a success, the effect ends. On a failure, the creature is petrified until freed by the greater restoration spell or other magic.'

    def attack_9_disintegration_ray_attack(self) -> str:
        """If the target is a creature, it must succeed on a DC 17 Dexterity saving throw or take 45 (10d8) force damage. If this damage reduces the creature to 0 hit points, its body becomes a pile of fine gray dust. If the target is a Large or smaller nonmagical object or creation of magical force, it is disintegrated without a saving throw. If the target is a Huge or larger object or creation of magical force, this ray disintegrates a 10-foot cube of it."""
        return 'If the target is a creature, it must succeed on a DC 17 Dexterity saving throw or take 45 (10d8) force damage. If this damage reduces the creature to 0 hit points, its body becomes a pile of fine gray dust. If the target is a Large or smaller nonmagical object or creation of magical force, it is disintegrated without a saving throw. If the target is a Huge or larger object or creation of magical force, this ray disintegrates a 10-foot cube of it.'

    def attack_10_death_ray_attack(self) -> str:
        """The targeted creature must succeed on a DC 17 Dexterity saving throw or take 55 (10d10) necrotic damage. The target dies if the ray reduces it to 0 hit points."""
        return 'The targeted creature must succeed on a DC 17 Dexterity saving throw or take 55 (10d10) necrotic damage. The target dies if the ray reduces it to 0 hit points.'

