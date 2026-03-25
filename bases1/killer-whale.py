# bases1/killer-whale.py
"""
KillerWhale creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=killer-whale
"""
from creature_base import GlobalCreatureBaseClass


class KillerWhale(GlobalCreatureBaseClass):
    """
    Huge beast creature - KillerWhale
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 90, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 10, 'CON': 13, 'INT': 3, 'WIS': 12, 'CHAR': 7, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 (natural armor) Hit Points  90 (12d12 + 12) Speed  0 ft.', 'legendary': False, 'size': 'Huge', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['echolocation', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def echolocation(self) -> str:
        """The whale can't use its blindsight while deafened.Hold Breath. The whale can hold its breath for 30 minutes.Keen Hearing. The whale has advantage on Wisdom (Perception) checks that rely on hearing."""
        return "The whale can't use its blindsight while deafened.Hold Breath. The whale can hold its breath for 30 minutes.Keen Hearing. The whale has advantage on Wisdom (Perception) checks that rely on hearing."

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 21 (5d6 + 4) piercing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 21 (5d6 + 4) piercing damage.'

