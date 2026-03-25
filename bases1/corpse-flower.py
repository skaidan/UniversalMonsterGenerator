# bases1/corpse-flower.py
"""
CorpseFlower creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=corpse-flower
"""
from creature_base import GlobalCreatureBaseClass


class CorpseFlower(GlobalCreatureBaseClass):
    """
    Large Plant creature - CorpseFlower
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 127, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 14, 'CON': 16, 'INT': 7, 'WIS': 15, 'CHAR': 3, 'armor_class': 12, 'alignment': 'typically Chaotic Evil Armor Class  12 Hit Points  127 (15d10 + 45) Speed  20 ft.', 'legendary': False, 'size': 'Large', 'type': 'Plant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

