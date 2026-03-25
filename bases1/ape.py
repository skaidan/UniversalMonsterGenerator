# bases1/ape.py
"""
Ape creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ape
"""
from creature_base import GlobalCreatureBaseClass


class Ape(GlobalCreatureBaseClass):
    """
    Medium beast creature - Ape
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 19, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 14, 'CON': 14, 'INT': 6, 'WIS': 12, 'CHAR': 7, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 Hit Points  19 (3d8 + 6) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'fist', 'rock']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The ape makes two fist attacks."""
        return 'The ape makes two fist attacks.'

    def fist_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) bludgeoning damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) bludgeoning damage.'

    def rock_attack(self) -> str:
        """Ranged Weapon Attack: +5 to hit, range 25/50 ft., one target. Hit: 6 (1d6 + 3) bludgeoning damage."""
        return 'Ranged Weapon Attack: +5 to hit, range 25/50 ft., one target. Hit: 6 (1d6 + 3) bludgeoning damage.'

