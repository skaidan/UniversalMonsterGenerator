# bases1/storm-giant-quintessent.py
"""
StormGiantQuintessent creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=storm-giant-quintessent
"""
from creature_base import GlobalCreatureBaseClass


class StormGiantQuintessent(GlobalCreatureBaseClass):
    """
    Huge Giant creature - StormGiantQuintessent
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 230, 'min_level': 1, 'level': 1, 'STR': 29, 'DEX': 14, 'CON': 20, 'INT': 17, 'WIS': 20, 'CHAR': 19, 'armor_class': 12, 'alignment': 'typically Chaotic Good Armor Class  12 Hit Points  230 (20d12 + 100) Speed  50 ft.', 'legendary': False, 'size': 'Huge', 'type': 'Giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

