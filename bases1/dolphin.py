# bases1/dolphin.py
"""
Dolphin creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dolphin
"""
from creature_base import GlobalCreatureBaseClass


class Dolphin(GlobalCreatureBaseClass):
    """
    Medium Beast creature - Dolphin
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 11, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 13, 'CON': 13, 'INT': 6, 'WIS': 12, 'CHAR': 7, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 (natural armor) Hit Points  11 (2d8 + 2) Speed  0 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['hold_breath', 'slam']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def hold_breath(self) -> str:
        """The dolphin can hold its breath for 20 minutes."""
        return 'The dolphin can hold its breath for 20 minutes.'

    def slam_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) bludgeoning damage. If the dolphin moved at least 30 feet straight toward the target immediately before the hit, the target takes an extra 3 (1d6) bludgeoning damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) bludgeoning damage. If the dolphin moved at least 30 feet straight toward the target immediately before the hit, the target takes an extra 3 (1d6) bludgeoning damage.'

