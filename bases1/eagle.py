# bases1/eagle.py
"""
Eagle creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=eagle
"""
from creature_base import GlobalCreatureBaseClass


class Eagle(GlobalCreatureBaseClass):
    """
    Small beast creature - Eagle
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 3, 'min_level': 1, 'level': 1, 'STR': 6, 'DEX': 15, 'CON': 10, 'INT': 2, 'WIS': 14, 'CHAR': 7, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 Hit Points  3 (1d6) Speed  10 ft.', 'legendary': False, 'size': 'Small', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_sight', 'talons']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_sight(self) -> str:
        """The eagle has advantage on Wisdom (Perception) checks that rely on sight."""
        return 'The eagle has advantage on Wisdom (Perception) checks that rely on sight.'

    def talons_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage.'

