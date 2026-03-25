# bases1/giant-poisonous-snake.py
"""
GiantPoisonousSnake creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-poisonous-snake
"""
from creature_base import GlobalCreatureBaseClass


class GiantPoisonousSnake(GlobalCreatureBaseClass):
    """
    Medium beast creature - GiantPoisonousSnake
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 11, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 18, 'CON': 13, 'INT': 2, 'WIS': 10, 'CHAR': 3, 'armor_class': 14, 'alignment': 'unaligned Armor Class  14 Hit Points  11 (2d8 + 2) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 6 (1d4 + 4) piercing damage, and the target must make a DC 11 Constitution saving throw, taking 10 (3d6) poison damage on a failed save, or half as much damage on a successful one."""
        return 'Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 6 (1d4 + 4) piercing damage, and the target must make a DC 11 Constitution saving throw, taking 10 (3d6) poison damage on a failed save, or half as much damage on a successful one.'

