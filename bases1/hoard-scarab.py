# bases1/hoard-scarab.py
"""
HoardScarab creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hoard-scarab
"""
from creature_base import GlobalCreatureBaseClass


class HoardScarab(GlobalCreatureBaseClass):
    """
    Tiny Monstrosity creature - HoardScarab
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 7, 'min_level': 1, 'level': 1, 'STR': 4, 'DEX': 16, 'CON': 11, 'INT': 3, 'WIS': 8, 'CHAR': 6, 'armor_class': 14, 'alignment': 'unaligned Armor Class  14 (natural armor) Hit Points  7 (3d4) Speed  20 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

