# bases1/walrus.py
"""
Walrus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=walrus
"""
from creature_base import GlobalCreatureBaseClass


class Walrus(GlobalCreatureBaseClass):
    """
    Large beast creature - Walrus
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 9, 'CON': 14, 'INT': 3, 'WIS': 11, 'CHAR': 4, 'armor_class': 9, 'alignment': 'unaligned Armor Class  9 Hit Points  22 (3d10 + 6) Speed  20 ft.', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

