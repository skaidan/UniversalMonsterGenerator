# bases1/hare.py
"""
Hare creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hare
"""
from creature_base import GlobalCreatureBaseClass


class Hare(GlobalCreatureBaseClass):
    """
    Tiny beast creature - Hare
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 1, 'min_level': 1, 'level': 1, 'STR': 1, 'DEX': 17, 'CON': 9, 'INT': 2, 'WIS': 11, 'CHAR': 4, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 Hit Points  1 (1d4 - 1) Speed  20 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

