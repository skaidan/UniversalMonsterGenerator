# bases1/constrictor-snake.py
"""
ConstrictorSnake creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=constrictor-snake
"""
from creature_base import GlobalCreatureBaseClass


class ConstrictorSnake(GlobalCreatureBaseClass):
    """
    Large beast creature - ConstrictorSnake
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 13, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 14, 'CON': 12, 'INT': 1, 'WIS': 10, 'CHAR': 3, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 Hit Points  13 (2d10 + 2) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['bite', 'constrict']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 5 (1d6 + 2) piercing damage.'

    def constrict_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 6 (1d8 + 2) bludgeoning damage, and the target is grappled (escape DC 14). Until this grapple ends, the creature is restrained, and the snake can't constrict another target."""
        return "Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 6 (1d8 + 2) bludgeoning damage, and the target is grappled (escape DC 14). Until this grapple ends, the creature is restrained, and the snake can't constrict another target."

