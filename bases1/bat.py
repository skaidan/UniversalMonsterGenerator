# bases1/bat.py
"""
Bat creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bat
"""
from creature_base import GlobalCreatureBaseClass


class Bat(GlobalCreatureBaseClass):
    """
    Tiny beast creature - Bat
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 1, 'min_level': 1, 'level': 1, 'STR': 2, 'DEX': 15, 'CON': 8, 'INT': 2, 'WIS': 12, 'CHAR': 4, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 Hit Points  1 (1d4 - 1) Speed  5 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['echolocation', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def echolocation(self) -> str:
        """The bat can't use its blindsight while deafened.Keen Hearing. The bat has advantage on Wisdom (Perception) checks that rely on hearing."""
        return "The bat can't use its blindsight while deafened.Keen Hearing. The bat has advantage on Wisdom (Perception) checks that rely on hearing."

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +0 to hit, reach 5 ft., one creature. Hit: 1 piercing damage."""
        return 'Melee Weapon Attack: +0 to hit, reach 5 ft., one creature. Hit: 1 piercing damage.'

