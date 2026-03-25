# bases1/duergar-stone-guard.py
"""
DuergarStoneGuard creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=duergar-stone-guard
"""
from creature_base import GlobalCreatureBaseClass


class DuergarStoneGuard(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Dwarf) creature - DuergarStoneGuard
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 39, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 11, 'CON': 14, 'INT': 11, 'WIS': 10, 'CHAR': 9, 'armor_class': 18, 'alignment': 'any alignment Armor Class  18 (chain mail', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Dwarf)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

