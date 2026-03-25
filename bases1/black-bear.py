# bases1/black-bear.py
"""
BlackBear creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=black-bear
"""
from creature_base import GlobalCreatureBaseClass


class BlackBear(GlobalCreatureBaseClass):
    """
    Medium beast creature - BlackBear
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 19, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 10, 'CON': 14, 'INT': 2, 'WIS': 12, 'CHAR': 7, 'armor_class': 11, 'alignment': 'unaligned Armor Class  11 (natural armor) Hit Points  19 (3d8 + 6) Speed  40 ft.', 'legendary': False, 'size': 'Medium', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_smell', 'multiattack', 'bite', 'claws']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_smell(self) -> str:
        """The bear has advantage on Wisdom (Perception) checks that rely on smell."""
        return 'The bear has advantage on Wisdom (Perception) checks that rely on smell.'

    def multiattack_attack(self) -> str:
        """The bear makes two attacks: one with its bite and one with its claws."""
        return 'The bear makes two attacks: one with its bite and one with its claws.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage.'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) slashing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 7 (2d4 + 2) slashing damage.'

