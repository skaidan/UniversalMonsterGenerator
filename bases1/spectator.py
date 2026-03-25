# bases1/spectator.py
"""
Spectator creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=spectator
"""
from creature_base import GlobalCreatureBaseClass


class Spectator(GlobalCreatureBaseClass):
    """
    Medium aberration creature - Spectator
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 39, 'min_level': 1, 'level': 1, 'STR': 8, 'DEX': 14, 'CON': 14, 'INT': 13, 'WIS': 14, 'CHAR': 11, 'armor_class': 14, 'alignment': 'lawful neutral Armor Class  14 (natural armor) Hit Points  39 (6d8 + 12) Speed  0 ft.', 'legendary': False, 'size': 'Medium', 'type': 'aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['bite', 'eye_rays', '&nbsp;_1-_confusion_ray', '&nbsp;_2-_paralyzing_ray', '&nbsp;_3-_fear_ray', '&nbsp;_4-_wounding_ray', 'create_food_and_water']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 2 (1d6 - 1) piercing damage."""
        return 'Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 2 (1d6 - 1) piercing damage.'

    def eye_rays_attack(self) -> str:
        """The spectator shoots up to two of the following magical eye rays at one or two creatures it can see within 90 feet of it. It can use each ray only once on a turn."""
        return 'The spectator shoots up to two of the following magical eye rays at one or two creatures it can see within 90 feet of it. It can use each ray only once on a turn.'

    def &nbsp;_1-_confusion_ray_attack(self) -> str:
        """The target must succeed on a DC 13 Wisdom saving throw, or it can't take reactions until the end of its next turn. On its turn, the target can't move, and it uses its action to make a melee or ranged attack against a randomly determined creature within range. If the target can't attack, it does nothing on its turn."""
        return "The target must succeed on a DC 13 Wisdom saving throw, or it can't take reactions until the end of its next turn. On its turn, the target can't move, and it uses its action to make a melee or ranged attack against a randomly determined creature within range. If the target can't attack, it does nothing on its turn."

    def &nbsp;_2-_paralyzing_ray_attack(self) -> str:
        """The target must succeed on a DC 13 Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'The target must succeed on a DC 13 Constitution saving throw or be paralyzed for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

    def &nbsp;_3-_fear_ray_attack(self) -> str:
        """The target must succeed on a DC 13 Wisdom saving throw or be frightened for 1 minute. The target can repeat the saving throw at the end of each of its turns, with disadvantage if the spectator is visible to the target, ending the effect on itself on a success."""
        return 'The target must succeed on a DC 13 Wisdom saving throw or be frightened for 1 minute. The target can repeat the saving throw at the end of each of its turns, with disadvantage if the spectator is visible to the target, ending the effect on itself on a success.'

    def &nbsp;_4-_wounding_ray_attack(self) -> str:
        """The target must make a DC 13 Constitution saving throw, taking 16 (3d10) necrotic damage on a failed save, or half as much damage on a successful one."""
        return 'The target must make a DC 13 Constitution saving throw, taking 16 (3d10) necrotic damage on a failed save, or half as much damage on a successful one.'

    def create_food_and_water_attack(self) -> str:
        """The spectator magically creates enough food and water to sustain itself for 24 hours."""
        return 'The spectator magically creates enough food and water to sustain itself for 24 hours.'

