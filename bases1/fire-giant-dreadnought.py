# bases1/fire-giant-dreadnought.py
"""
FireGiantDreadnought creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fire-giant-dreadnought
"""
from creature_base import GlobalCreatureBaseClass


class FireGiantDreadnought(GlobalCreatureBaseClass):
    """
    Huge Giant creature - FireGiantDreadnought
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 187, 'min_level': 1, 'level': 1, 'STR': 27, 'DEX': 9, 'CON': 23, 'INT': 8, 'WIS': 10, 'CHAR': 11, 'armor_class': 21, 'alignment': 'typically Lawful Evil Armor Class  21 (plate', 'legendary': False, 'size': 'Huge', 'type': 'Giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

