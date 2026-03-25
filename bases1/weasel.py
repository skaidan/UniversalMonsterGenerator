# bases1/weasel.py
"""
Weasel creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=weasel
"""
from creature_base import GlobalCreatureBaseClass


class Weasel(GlobalCreatureBaseClass):
    """
    Tiny beast creature - Weasel
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 1, 'min_level': 1, 'level': 1, 'STR': 3, 'DEX': 16, 'CON': 8, 'INT': 2, 'WIS': 12, 'CHAR': 3, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 Hit Points  1 (1d4 - 1) Speed  30 ft. STR 3 (-4) DEX 16 (+3) CON 8 (-1) INT 2 (-4) WIS 12 (+1) CHA 3 (-4) Skills  Perception +3', 'legendary': False, 'size': 'Tiny', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_hearing_and_smell', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_hearing_and_smell(self) -> str:
        """The weasel has advantage on Wisdom (Perception) checks that rely on hearing or smell."""
        return 'The weasel has advantage on Wisdom (Perception) checks that rely on hearing or smell.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1 piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 1 piercing damage.'

