# bases1/roper.py
"""
Roper creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=roper
"""
from creature_base import GlobalCreatureBaseClass


class Roper(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - Roper
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 93, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 8, 'CON': 17, 'INT': 7, 'WIS': 16, 'CHAR': 6, 'armor_class': 20, 'alignment': 'neutral evil Armor Class  20 (natural armor) Hit Points  93 (11d10 + 33) Speed  10 ft.', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['false_appearance', 'multiattack', 'bite', 'tendril', 'reel']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def false_appearance(self) -> str:
        """While the roper remains motionless, it is indistinguishable from a normal cave formation, such as a stalagmite.Grasping Tendrils. The roper can have up to six tendrils at a time. Each tendril can be a"""
        return 'While the roper remains motionless, it is indistinguishable from a normal cave formation, such as a stalagmite.Grasping Tendrils. The roper can have up to six tendrils at a time. Each tendril can be a'

    def multiattack_attack(self) -> str:
        """The roper makes four attacks with its tendrils, uses Reel, and makes one attack with its bite."""
        return 'The roper makes four attacks with its tendrils, uses Reel, and makes one attack with its bite.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 22 (4d8 + 4) piercing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 22 (4d8 + 4) piercing damage.'

    def tendril_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 50 ft., one creature. Hit: The target is grappled (escape DC 15). Until the grapple ends, the target is restrained and has disadvantage on Strength checks and Strength saving throws, and the roper can't use the same tendril on another target."""
        return "Melee Weapon Attack: +7 to hit, reach 50 ft., one creature. Hit: The target is grappled (escape DC 15). Until the grapple ends, the target is restrained and has disadvantage on Strength checks and Strength saving throws, and the roper can't use the same tendril on another target."

    def reel_attack(self) -> str:
        """The roper pulls each creature grappled by it up to 25 feet straight toward it."""
        return 'The roper pulls each creature grappled by it up to 25 feet straight toward it.'

