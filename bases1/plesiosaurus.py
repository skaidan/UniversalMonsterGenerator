# bases1/plesiosaurus.py
"""
Plesiosaurus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=plesiosaurus
"""
from creature_base import GlobalCreatureBaseClass


class Plesiosaurus(GlobalCreatureBaseClass):
    """
    Large beast creature - Plesiosaurus
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 68, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 15, 'CON': 16, 'INT': 2, 'WIS': 12, 'CHAR': 5, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 (natural armor) Hit Points  68 (8d10 + 24) Speed  20 ft.', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['hold_breath', 'bite']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def hold_breath(self) -> str:
        """The plesiosaurus can hold its breath for 1 hour."""
        return 'The plesiosaurus can hold its breath for 1 hour.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 14 (3d6 + 4) piercing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 14 (3d6 + 4) piercing damage.'

