# bases1/hippogriff.py
"""
Hippogriff creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hippogriff
"""
from creature_base import GlobalCreatureBaseClass


class Hippogriff(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - Hippogriff
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 19, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 13, 'CON': 13, 'INT': 2, 'WIS': 12, 'CHAR': 8, 'armor_class': 11, 'alignment': 'unaligned Armor Class  11 Hit Points  19 (3d10 + 3) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_sight', 'multiattack', 'beak', 'claws']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_sight(self) -> str:
        """The hippogriff has advantage on Wisdom (Perception) checks that rely on sight."""
        return 'The hippogriff has advantage on Wisdom (Perception) checks that rely on sight.'

    def multiattack_attack(self) -> str:
        """The hippogriff makes two attacks: one with its beak and one with its claws."""
        return 'The hippogriff makes two attacks: one with its beak and one with its claws.'

    def beak_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d10 + 3) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 8 (1d10 + 3) piercing damage.'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) slashing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) slashing damage.'

