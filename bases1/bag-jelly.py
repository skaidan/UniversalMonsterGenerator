# bases1/bag-jelly.py
"""
BagJelly creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bag-jelly
"""
from creature_base import GlobalCreatureBaseClass


class BagJelly(GlobalCreatureBaseClass):
    """
    Medium Ooze creature - BagJelly
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 42, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 6, 'CON': 19, 'INT': 2, 'WIS': 7, 'CHAR': 2, 'armor_class': 8, 'alignment': 'unaligned Armor Class  8 Hit Points  42 (5d8 + 20) Speed  10 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Ooze', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

