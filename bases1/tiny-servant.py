# bases1/tiny-servant.py
"""
TinyServant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=tiny-servant
"""
from creature_base import GlobalCreatureBaseClass


class TinyServant(GlobalCreatureBaseClass):
    """
    Tiny construct creature - TinyServant
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 10, 'min_level': 1, 'level': 1, 'STR': 4, 'DEX': 16, 'CON': 10, 'INT': 2, 'WIS': 10, 'CHAR': 1, 'armor_class': 15, 'alignment': 'unaligned Armor Class  15 (natural armor) Hit Points  10 (4d4) Speed  30 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['slam']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def slam_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) bludgeoning damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) bludgeoning damage.'

