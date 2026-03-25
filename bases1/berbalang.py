# bases1/berbalang.py
"""
Berbalang creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=berbalang
"""
from creature_base import GlobalCreatureBaseClass


class Berbalang(GlobalCreatureBaseClass):
    """
    Medium Aberration creature - Berbalang
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 49, 'min_level': 1, 'level': 1, 'STR': 9, 'DEX': 16, 'CON': 9, 'INT': 17, 'WIS': 11, 'CHAR': 10, 'armor_class': 14, 'alignment': 'typically Neutral Evil Armor Class  14 (natural armor) Hit Points  49 (14d8 - 14) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

