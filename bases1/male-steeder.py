# bases1/male-steeder.py
"""
MaleSteeder creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=male-steeder
"""
from creature_base import GlobalCreatureBaseClass


class MaleSteeder(GlobalCreatureBaseClass):
    """
    Medium Monstrosity creature - MaleSteeder
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 13, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 12, 'CON': 14, 'INT': 2, 'WIS': 10, 'CHAR': 3, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 (natural armor) Hit Points  13 (2d8 + 4) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['extraordinary_leap', 'bite', 'sticky_leg']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def extraordinary_leap(self) -> str:
        """The distance of the steeder's long jumps is tripled; every foot of its walking speed that it spends on the jump allows it to jump 3 feet.Spider Climb. The steeder can climb difficult surfaces, includi"""
        return "The distance of the steeder's long jumps is tripled; every foot of its walking speed that it spends on the jump allows it to jump 3 feet.Spider Climb. The steeder can climb difficult surfaces, includi"

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) piercing damage plus 4 (1d8) poison damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) piercing damage plus 4 (1d8) poison damage.'

    def sticky_leg_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one Small or Tiny creature. Hit: The target is stuck to the steeder's leg and grappled (escape DC 12). The steeder can have only one creature grappled at a time."""
        return "Melee Weapon Attack: +4 to hit, reach 5 ft., one Small or Tiny creature. Hit: The target is stuck to the steeder's leg and grappled (escape DC 12). The steeder can have only one creature grappled at a time."

