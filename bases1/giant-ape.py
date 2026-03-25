# bases1/giant-ape.py
"""
GiantApe creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-ape
"""
from creature_base import GlobalCreatureBaseClass


class GiantApe(GlobalCreatureBaseClass):
    """
    Huge beast creature - GiantApe
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 157, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 14, 'CON': 18, 'INT': 7, 'WIS': 12, 'CHAR': 7, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 Hit Points  157 (15d12 + 60) Speed  40 ft.', 'legendary': False, 'size': 'Huge', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'fist', 'rock']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The ape makes two fist attacks."""
        return 'The ape makes two fist attacks.'

    def fist_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 22 (3d10 + 6) bludgeoning damage."""
        return 'Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 22 (3d10 + 6) bludgeoning damage.'

    def rock_attack(self) -> str:
        """Ranged Weapon Attack: +9 to hit, range 50/100 ft., one target. Hit: 30 (7d6 + 6) bludgeoning damage."""
        return 'Ranged Weapon Attack: +9 to hit, range 50/100 ft., one target. Hit: 30 (7d6 + 6) bludgeoning damage.'

