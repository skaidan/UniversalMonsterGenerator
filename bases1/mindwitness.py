# bases1/mindwitness.py
"""
Mindwitness creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mindwitness
"""
from creature_base import GlobalCreatureBaseClass


class Mindwitness(GlobalCreatureBaseClass):
    """
    Large Aberration creature - Mindwitness
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 75, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 14, 'CON': 14, 'INT': 15, 'WIS': 15, 'CHAR': 10, 'armor_class': 15, 'alignment': 'typically Lawful Neutral Armor Class  15 (natural armor) Hit Points  75 (10d10 + 20) Speed  0 ft.', 'legendary': False, 'size': 'Large', 'type': 'Aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

