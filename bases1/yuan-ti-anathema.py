# bases1/yuan-ti-anathema.py
"""
YuanTiAnathema creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yuan-ti-anathema
"""
from creature_base import GlobalCreatureBaseClass


class YuanTiAnathema(GlobalCreatureBaseClass):
    """
    Huge Monstrosity creature - YuanTiAnathema
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 189, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 13, 'CON': 19, 'INT': 19, 'WIS': 17, 'CHAR': 20, 'armor_class': 16, 'alignment': 'typically Neutral Evil Armor Class  16 (natural armor) Hit Points  189 (18d12 + 72) Speed  40 ft.', 'legendary': False, 'size': 'Huge', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

