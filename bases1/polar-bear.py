# bases1/polar-bear.py
"""
PolarBear creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=polar-bear
"""
from creature_base import GlobalCreatureBaseClass


class PolarBear(GlobalCreatureBaseClass):
    """
    Large beast creature - PolarBear
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 42, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 10, 'CON': 16, 'INT': 2, 'WIS': 13, 'CHAR': 7, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 (natural armor) Hit Points  42 (5d10 + 15) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_smell', 'multiattack', 'bite', 'claws']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_smell(self) -> str:
        """The bear has advantage on Wisdom (Perception) checks that rely on smell."""
        return 'The bear has advantage on Wisdom (Perception) checks that rely on smell.'

    def multiattack_attack(self) -> str:
        """The bear makes two attacks: one with its bite and one with its claws."""
        return 'The bear makes two attacks: one with its bite and one with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 9 (1d8 + 5) piercing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 9 (1d8 + 5) piercing damage.'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage.'

