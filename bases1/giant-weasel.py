# bases1/giant-weasel.py
"""
GiantWeasel creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-weasel
"""
from creature_base import GlobalCreatureBaseClass


class GiantWeasel(GlobalCreatureBaseClass):
    """
    Medium beast creature - GiantWeasel
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 9, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 16, 'CON': 10, 'INT': 4, 'WIS': 12, 'CHAR': 5, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 Hit Points  9 (2d8) Speed  40 ft. STR 11 (+0) DEX 16 (+3) CON 10 (+0) INT 4 (-3) WIS 12 (+1) CHA 5 (-3) Skills  Perception +3', 'legendary': False, 'size': 'Medium', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_hearing_and_smell', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_hearing_and_smell(self) -> str:
        """The weasel has advantage on Wisdom (Perception) checks that rely on hearing or smell."""
        return 'The weasel has advantage on Wisdom (Perception) checks that rely on hearing or smell.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) piercing damage."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d4 + 3) piercing damage.'

