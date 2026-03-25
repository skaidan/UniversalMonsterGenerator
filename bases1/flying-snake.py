# bases1/flying-snake.py
"""
FlyingSnake creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=flying-snake
"""
from creature_base import GlobalCreatureBaseClass


class FlyingSnake(GlobalCreatureBaseClass):
    """
    Tiny beast creature - FlyingSnake
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 5, 'min_level': 1, 'level': 1, 'STR': 4, 'DEX': 18, 'CON': 11, 'INT': 2, 'WIS': 12, 'CHAR': 5, 'armor_class': 14, 'alignment': 'unaligned Armor Class  14 Hit Points  5 (2d4) Speed  30 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['flyby', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def flyby(self) -> str:
        """The snake doesn't provoke opportunity attacks when it flies out of an enemy's reach."""
        return "The snake doesn't provoke opportunity attacks when it flies out of an enemy's reach."

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 1 piercing damage plus 7 (3d4) poison damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 1 piercing damage plus 7 (3d4) poison damage.'

