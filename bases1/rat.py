# bases1/rat.py
"""
Rat creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=rat
"""
from creature_base import GlobalCreatureBaseClass


class Rat(GlobalCreatureBaseClass):
    """
    Tiny beast creature - Rat
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 1, 'min_level': 1, 'level': 1, 'STR': 2, 'DEX': 11, 'CON': 9, 'INT': 2, 'WIS': 10, 'CHAR': 4, 'armor_class': 10, 'alignment': 'unaligned Armor Class  10 Hit Points  1 (1d4 - 1) Speed  20 ft. STR 2 (-4) DEX 11 (+0) CON 9 (-1) INT 2 (-4) WIS 10 (+0) CHA 4 (-3) Senses  darkvision 30 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_smell', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_smell(self) -> str:
        """The rat has advantage on Wisdom (Perception) checks that rely on smell."""
        return 'The rat has advantage on Wisdom (Perception) checks that rely on smell.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +0 to hit, reach 5 ft., one target. Hit: 1 piercing damage."""
        return 'Melee Weapon Attack: +0 to hit, reach 5 ft., one target. Hit: 1 piercing damage.'

