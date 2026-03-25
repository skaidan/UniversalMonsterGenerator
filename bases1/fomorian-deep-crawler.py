# bases1/fomorian-deep-crawler.py
"""
FomorianDeepCrawler creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fomorian-deep-crawler
"""
from creature_base import GlobalCreatureBaseClass


class FomorianDeepCrawler(GlobalCreatureBaseClass):
    """
    Huge Giant creature - FomorianDeepCrawler
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 184, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 15, 'CON': 20, 'INT': 9, 'WIS': 17, 'CHAR': 6, 'armor_class': 14, 'alignment': 'any alignment Armor Class  14 (natural armor) Hit Points  184 (16d12 + 80) Speed  30 ft.', 'legendary': False, 'size': 'Huge', 'type': 'Giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

