# bases1/griffon.py
"""
Griffon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=griffon
"""
from creature_base import GlobalCreatureBaseClass


class Griffon(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - Griffon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 59, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 15, 'CON': 16, 'INT': 2, 'WIS': 13, 'CHAR': 8, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 Hit Points  59 (7d10 + 21) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_sight', 'multiattack', 'beak', 'claws']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_sight(self) -> str:
        """The griffon has advantage on Wisdom (Perception) checks that rely on sight."""
        return 'The griffon has advantage on Wisdom (Perception) checks that rely on sight.'

    def multiattack_attack(self) -> str:
        """The griffon makes two attacks: one with its beak and one with its claws."""
        return 'The griffon makes two attacks: one with its beak and one with its claws.'

    def beak_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) piercing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) piercing damage.'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) slashing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) slashing damage.'

