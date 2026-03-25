# bases1/grinning-cat.py
"""
GrinningCat creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=grinning-cat
"""
from creature_base import GlobalCreatureBaseClass


class GrinningCat(GlobalCreatureBaseClass):
    """
    Large Fey creature - GrinningCat
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 45, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 15, 'CON': 13, 'INT': 15, 'WIS': 14, 'CHAR': 16, 'armor_class': 12, 'alignment': 'typically Chaotic Neutral Armor Class  12 Hit Points  45 (7d10 + 7) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'Fey', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

