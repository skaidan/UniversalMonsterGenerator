# bases1/gazer.py
"""
Gazer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gazer
"""
from creature_base import GlobalCreatureBaseClass


class Gazer(GlobalCreatureBaseClass):
    """
    Tiny Aberration (Beholder) creature - Gazer
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 13, 'min_level': 1, 'level': 1, 'STR': 3, 'DEX': 17, 'CON': 14, 'INT': 3, 'WIS': 10, 'CHAR': 7, 'armor_class': 13, 'alignment': 'typically Neutral Evil Armor Class  13 Hit Points  13 (3d4 + 6) Speed  0 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'Aberration (Beholder)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['mimicry', 'bite', 'eye_rays', '&nbsp;_1-_dazing_ray', '&nbsp;_2-_fear_ray', '&nbsp;_3-_frost_ray', '&nbsp;_4-_telekinetic_ray']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def mimicry(self) -> str:
        """The gazer can mimic simple sounds of speech it has heard, in any language. A creature that hears the sounds can tell they are imitations with a successful DC 10 Wisdom (Insight) check."""
        return 'The gazer can mimic simple sounds of speech it has heard, in any language. A creature that hears the sounds can tell they are imitations with a successful DC 10 Wisdom (Insight) check.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1 piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1 piercing damage.'

    def eye_rays_attack(self) -> str:
        """The gazer shoots two of the following magical eye rays at random (roll two d4s, and reroll duplicates), choosing one or two targets it can see within 60 feet of it:"""
        return 'The gazer shoots two of the following magical eye rays at random (roll two d4s, and reroll duplicates), choosing one or two targets it can see within 60 feet of it:'

    def &nbsp;_1-_dazing_ray_attack(self) -> str:
        """The targeted creature must succeed on a DC 12 Wisdom saving throw or be charmed until the start of the gazer's next turn. While the target is charmed in this way, its speed is halved, and it has disadvantage on attack rolls."""
        return "The targeted creature must succeed on a DC 12 Wisdom saving throw or be charmed until the start of the gazer's next turn. While the target is charmed in this way, its speed is halved, and it has disadvantage on attack rolls."

    def &nbsp;_2-_fear_ray_attack(self) -> str:
        """The targeted creature must succeed on a DC 12 Wisdom saving throw or be frightened until the start of the gazer's next turn."""
        return "The targeted creature must succeed on a DC 12 Wisdom saving throw or be frightened until the start of the gazer's next turn."

    def &nbsp;_3-_frost_ray_attack(self) -> str:
        """The target must succeed on a DC 12 Dexterity saving throw or take 10 (3d6) cold damage."""
        return 'The target must succeed on a DC 12 Dexterity saving throw or take 10 (3d6) cold damage.'

    def &nbsp;_4-_telekinetic_ray_attack(self) -> str:
        """If the target is a creature that is Medium or smaller, it must succeed on a DC 12 Strength saving throw or be moved up to 30 feet directly away from the gazer. If the target is a Tiny object that isn't being worn or carried, the gazer moves it up to 30 feet in any direction. The gazer can also exert fine control on objects with this ray, such as manipulating a simple tool or opening a container."""
        return "If the target is a creature that is Medium or smaller, it must succeed on a DC 12 Strength saving throw or be moved up to 30 feet directly away from the gazer. If the target is a Tiny object that isn't being worn or carried, the gazer moves it up to 30 feet in any direction. The gazer can also exert fine control on objects with this ray, such as manipulating a simple tool or opening a container."

