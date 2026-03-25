# bases1/gauth.py
"""
Gauth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gauth
"""
from creature_base import GlobalCreatureBaseClass


class Gauth(GlobalCreatureBaseClass):
    """
    Medium Aberration (Beholder) creature - Gauth
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 52, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 14, 'CON': 16, 'INT': 15, 'WIS': 15, 'CHAR': 13, 'armor_class': 15, 'alignment': 'typically Lawful Evil Armor Class  15 (natural armor) Hit Points  52 (7d8 + 21) Speed  0 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Aberration (Beholder)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['death_throes', 'bite', 'eye_rays', '&nbsp;_1-_devour_magic_ray', '&nbsp;_2-_enervation_ray', '&nbsp;_3-_fire_ray', '&nbsp;_4-_paralyzing_ray', '&nbsp;_5-_pushing_ray', '&nbsp;_6-_sleep_ray']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def death_throes(self) -> str:
        """When the gauth dies, the magical energy within it explodes, and each creature within 10 feet of it must make a DC 14 Dexterity saving throw, taking 13 (3d8) force damage on a failed save, or half as m"""
        return 'When the gauth dies, the magical energy within it explodes, and each creature within 10 feet of it must make a DC 14 Dexterity saving throw, taking 13 (3d8) force damage on a failed save, or half as m'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 9 (2d8) piercing damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 9 (2d8) piercing damage.'

    def eye_rays_attack(self) -> str:
        """The gauth shoots three of the following magical eye rays at random (roll three d6s, and reroll duplicates), targeting one to three creatures it can see within 120 feet of it:"""
        return 'The gauth shoots three of the following magical eye rays at random (roll three d6s, and reroll duplicates), targeting one to three creatures it can see within 120 feet of it:'

    def &nbsp;_1-_devour_magic_ray_attack(self) -> str:
        """The target must succeed on a DC 14 Dexterity saving throw or have one of its magic items lose all magical properties until the start of the gauth's next turn. If the object is a charged item, it also loses 1d4 charges. Determine the affected item randomly, ignoring single-use items such as potions and scrolls."""
        return "The target must succeed on a DC 14 Dexterity saving throw or have one of its magic items lose all magical properties until the start of the gauth's next turn. If the object is a charged item, it also loses 1d4 charges. Determine the affected item randomly, ignoring single-use items such as potions and scrolls."

    def &nbsp;_2-_enervation_ray_attack(self) -> str:
        """The target must make a DC 14 Constitution saving throw, taking 18 (4d8) necrotic damage on a failed save, or half as much damage on a successful one."""
        return 'The target must make a DC 14 Constitution saving throw, taking 18 (4d8) necrotic damage on a failed save, or half as much damage on a successful one.'

    def &nbsp;_3-_fire_ray_attack(self) -> str:
        """The target must succeed on a DC 14 Dexterity saving throw or take 22 (4d10) fire damage."""
        return 'The target must succeed on a DC 14 Dexterity saving throw or take 22 (4d10) fire damage.'

    def &nbsp;_4-_paralyzing_ray_attack(self) -> str:
        """The target must succeed on a DC 14 Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'The target must succeed on a DC 14 Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

    def &nbsp;_5-_pushing_ray_attack(self) -> str:
        """The target must succeed on a DC 14 Strength saving throw or be pushed up to 15 feet away from the gauth and have its speed halved until the start of the gauth's next turn."""
        return "The target must succeed on a DC 14 Strength saving throw or be pushed up to 15 feet away from the gauth and have its speed halved until the start of the gauth's next turn."

    def &nbsp;_6-_sleep_ray_attack(self) -> str:
        """The target must succeed on a DC 14 Wisdom saving throw or fall asleep and remain unconscious for 1 minute. The target awakens if it takes damage or another creature takes an action to wake it. This ray has no effect on Constructs and Undead."""
        return 'The target must succeed on a DC 14 Wisdom saving throw or fall asleep and remain unconscious for 1 minute. The target awakens if it takes damage or another creature takes an action to wake it. This ray has no effect on Constructs and Undead.'

