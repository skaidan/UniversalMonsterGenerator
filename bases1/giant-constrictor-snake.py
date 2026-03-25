# bases1/giant-constrictor-snake.py
"""
GiantConstrictorSnake creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-constrictor-snake
"""
from creature_base import GlobalCreatureBaseClass


class GiantConstrictorSnake(GlobalCreatureBaseClass):
    """
    Huge beast creature - GiantConstrictorSnake
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 60, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 14, 'CON': 12, 'INT': 1, 'WIS': 10, 'CHAR': 3, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 Hit Points  60 (8d12 + 8) Speed  30 ft.', 'legendary': False, 'size': 'Huge', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['bite', 'constrict']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 10 ft., one creature. Hit: 11 (2d6 + 4) piercing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 10 ft., one creature. Hit: 11 (2d6 + 4) piercing damage.'

    def constrict_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one creature. Hit: 13 (2d8 + 4) bludgeoning damage, and the target is grappled (escape DC 16). Until this grapple ends, the creature is restrained, and the snake can't constrict another target."""
        return "Melee Weapon Attack: +6 to hit, reach 5 ft., one creature. Hit: 13 (2d8 + 4) bludgeoning damage, and the target is grappled (escape DC 16). Until this grapple ends, the creature is restrained, and the snake can't constrict another target."

