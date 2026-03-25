# bases1/female-steeder.py
"""
FemaleSteeder creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=female-steeder
"""
from creature_base import GlobalCreatureBaseClass


class FemaleSteeder(GlobalCreatureBaseClass):
    """
    Large Monstrosity creature - FemaleSteeder
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 30, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 16, 'CON': 14, 'INT': 2, 'WIS': 10, 'CHAR': 3, 'armor_class': 14, 'alignment': 'unaligned Armor Class  14 (natural armor) Hit Points  30 (4d10 + 8) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['extraordinary_leap', 'bite', 'sticky_leg']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def extraordinary_leap(self) -> str:
        """The distance of the steeder's long jumps is tripled; every foot of its walking speed that it spends on the jump allows it to move 3 feet.Spider Climb. The steeder can climb difficult surfaces, includi"""
        return "The distance of the steeder's long jumps is tripled; every foot of its walking speed that it spends on the jump allows it to move 3 feet.Spider Climb. The steeder can climb difficult surfaces, includi"

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage plus 9 (2d8) poison damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage plus 9 (2d8) poison damage.'

    def sticky_leg_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one Medium or smaller creature. Hit: The target is stuck to the steeder's leg and grappled (escape DC 12). The steeder can have only one creature grappled at a time."""
        return "Melee Weapon Attack: +5 to hit, reach 5 ft., one Medium or smaller creature. Hit: The target is stuck to the steeder's leg and grappled (escape DC 12). The steeder can have only one creature grappled at a time."

