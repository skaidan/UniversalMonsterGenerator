# bases1/poisonous-snake.py
"""
PoisonousSnake creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=poisonous-snake
"""
from creature_base import GlobalCreatureBaseClass


class PoisonousSnake(GlobalCreatureBaseClass):
    """
    Tiny beast creature - PoisonousSnake
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 2, 'min_level': 1, 'level': 1, 'STR': 2, 'DEX': 16, 'CON': 11, 'INT': 1, 'WIS': 10, 'CHAR': 3, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 Hit Points  2 (1d4) Speed  30 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1 piercing damage, and the target must make a DC 10 Constitution saving throw, taking 5 (2d4) poison damage on a failed save, or half as much damage on a successful one."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1 piercing damage, and the target must make a DC 10 Constitution saving throw, taking 5 (2d4) poison damage on a failed save, or half as much damage on a successful one.'

