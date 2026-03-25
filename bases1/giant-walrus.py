# bases1/giant-walrus.py
"""
GiantWalrus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-walrus
"""
from creature_base import GlobalCreatureBaseClass


class GiantWalrus(GlobalCreatureBaseClass):
    """
    Huge beast creature - GiantWalrus
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 55, 'min_level': 1, 'level': 1, 'STR': 22, 'DEX': 9, 'CON': 16, 'INT': 3, 'WIS': 11, 'CHAR': 4, 'armor_class': 9, 'alignment': 'unaligned Armor Class  9 Hit Points  55 (9d12 + 27) Speed  20 ft.', 'legendary': False, 'size': 'Huge', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

