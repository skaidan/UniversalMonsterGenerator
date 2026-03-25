# bases1/fox.py
"""
Fox creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fox
"""
from creature_base import GlobalCreatureBaseClass


class Fox(GlobalCreatureBaseClass):
    """
    Tiny beast creature - Fox
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 2, 'min_level': 1, 'level': 1, 'STR': 2, 'DEX': 16, 'CON': 11, 'INT': 3, 'WIS': 12, 'CHAR': 6, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 Hit Points  2 (1d4) Speed  30 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

