# bases1/young-deep-dragon.py
"""
YoungDeepDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=young-deep-dragon
"""
from creature_base import GlobalCreatureBaseClass


class YoungDeepDragon(GlobalCreatureBaseClass):
    """
    Large Dragon creature - YoungDeepDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 93, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 13, 'CON': 16, 'INT': 12, 'WIS': 14, 'CHAR': 16, 'armor_class': 16, 'alignment': 'typically Neutral Evil Armor Class  16 (natural armor) Hit Points  93 (11d10 + 33) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'Dragon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

