# bases1/giant-bat.py
"""
GiantBat creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-bat
"""
from creature_base import GlobalCreatureBaseClass


class GiantBat(GlobalCreatureBaseClass):
    """
    Large beast creature - GiantBat
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 16, 'CON': 11, 'INT': 2, 'WIS': 12, 'CHAR': 6, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 Hit Points  22 (4d10) Speed  10 ft.', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['echolocation', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def echolocation(self) -> str:
        """The bat can't use its blindsight while deafened.Keen Hearing. The bat has advantage on Wisdom (Perception) checks that rely on hearing."""
        return "The bat can't use its blindsight while deafened.Keen Hearing. The bat has advantage on Wisdom (Perception) checks that rely on hearing."

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 5 (1d6 + 2) piercing damage.'

