# bases1/hawk.py
"""
Hawk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hawk
"""
from creature_base import GlobalCreatureBaseClass


class Hawk(GlobalCreatureBaseClass):
    """
    Tiny beast creature - Hawk
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 1, 'min_level': 1, 'level': 1, 'STR': 5, 'DEX': 16, 'CON': 8, 'INT': 2, 'WIS': 14, 'CHAR': 6, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 Hit Points  1 (1d4 - 1) Speed  10 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_sight', 'talons']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_sight(self) -> str:
        """The hawk has advantage on Wisdom (Perception) checks that rely on sight."""
        return 'The hawk has advantage on Wisdom (Perception) checks that rely on sight.'

    def talons_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1 slashing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1 slashing damage.'

