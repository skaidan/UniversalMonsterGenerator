# bases1/gem-stalker.py
"""
GemStalker creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gem-stalker
"""
from creature_base import GlobalCreatureBaseClass


class GemStalker(GlobalCreatureBaseClass):
    """
    Large Monstrosity creature - GemStalker
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 67, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 15, 'CON': 14, 'INT': 15, 'WIS': 10, 'CHAR': 6, 'armor_class': 17, 'alignment': 'typically Neutral Armor Class  17 (natural armor) Hit Points  67 (9d10 + 18) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

