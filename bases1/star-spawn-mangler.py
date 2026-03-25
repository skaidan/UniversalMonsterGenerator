# bases1/star-spawn-mangler.py
"""
StarSpawnMangler creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=star-spawn-mangler
"""
from creature_base import GlobalCreatureBaseClass


class StarSpawnMangler(GlobalCreatureBaseClass):
    """
    Medium Aberration creature - StarSpawnMangler
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 71, 'min_level': 1, 'level': 1, 'STR': 8, 'DEX': 18, 'CON': 12, 'INT': 11, 'WIS': 12, 'CHAR': 7, 'armor_class': 14, 'alignment': 'typically Chaotic Evil Armor Class  14 Hit Points  71 (13d8 + 13) Speed  40 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

