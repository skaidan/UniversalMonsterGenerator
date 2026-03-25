# bases1/cat.py
"""
Cat creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cat
"""
from creature_base import GlobalCreatureBaseClass


class Cat(GlobalCreatureBaseClass):
    """
    Tiny beast creature - Cat
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 2, 'min_level': 1, 'level': 1, 'STR': 3, 'DEX': 15, 'CON': 10, 'INT': 3, 'WIS': 12, 'CHAR': 7, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 Hit Points  2 (1d4) Speed  40 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_smell', 'claws']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_smell(self) -> str:
        """The cat has advantage on Wisdom (Perception) checks that rely on smell."""
        return 'The cat has advantage on Wisdom (Perception) checks that rely on smell.'

    def claws_attack(self) -> str:
        """Melee Weapon Attack: +0 to hit, reach 5 ft., one target. Hit: 1 slashing damage."""
        return 'Melee Weapon Attack: +0 to hit, reach 5 ft., one target. Hit: 1 slashing damage.'

