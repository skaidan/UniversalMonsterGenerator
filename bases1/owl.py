# bases1/owl.py
"""
Owl creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=owl
"""
from creature_base import GlobalCreatureBaseClass


class Owl(GlobalCreatureBaseClass):
    """
    Tiny beast creature - Owl
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 1, 'min_level': 1, 'level': 1, 'STR': 3, 'DEX': 13, 'CON': 8, 'INT': 2, 'WIS': 12, 'CHAR': 7, 'armor_class': 11, 'alignment': 'unaligned Armor Class  11 Hit Points  1 (1d4 - 1) Speed  5 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['flyby', 'talons']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def flyby(self) -> str:
        """The owl doesn't provoke opportunity attacks when it flies out of an enemy's reach.Keen Hearing and Sight. The owl has advantage on Wisdom (Perception) checks that rely on hearing or sight."""
        return "The owl doesn't provoke opportunity attacks when it flies out of an enemy's reach.Keen Hearing and Sight. The owl has advantage on Wisdom (Perception) checks that rely on hearing or sight."

    def talons_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 1 slashing damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 1 slashing damage.'

