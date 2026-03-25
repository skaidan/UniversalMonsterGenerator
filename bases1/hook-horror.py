# bases1/hook-horror.py
"""
HookHorror creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hook-horror
"""
from creature_base import GlobalCreatureBaseClass


class HookHorror(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - HookHorror
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 75, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 10, 'CON': 15, 'INT': 6, 'WIS': 12, 'CHAR': 7, 'armor_class': 15, 'alignment': 'neutral Armor Class  15 (natural armor) Hit Points  75 (10d10 + 20) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['echolocation', 'multiattack', 'hook']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def echolocation(self) -> str:
        """The hook horror can't use its blindsight while deafened.Keen Hearing. The hook horror has advantage on Wisdom (Perception) checks that rely on hearing."""
        return "The hook horror can't use its blindsight while deafened.Keen Hearing. The hook horror has advantage on Wisdom (Perception) checks that rely on hearing."

    def multiattack_attack(self) -> str:
        """The hook horror makes two hook attacks."""
        return 'The hook horror makes two hook attacks.'

    def hook_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 11 (2d6 + 4) piercing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 11 (2d6 + 4) piercing damage.'

