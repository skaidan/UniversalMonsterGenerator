# bases1/hellwasp.py
"""
Hellwasp creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hellwasp
"""
from creature_base import GlobalCreatureBaseClass


class Hellwasp(GlobalCreatureBaseClass):
    """
    Large fiend creature - Hellwasp
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 52, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 15, 'CON': 12, 'INT': 10, 'WIS': 10, 'CHAR': 7, 'armor_class': 19, 'alignment': 'lawful evil Armor Class  19 (natural armor) Hit Points  52 (8d10 + 8) Speed  10 ft.', 'legendary': False, 'size': 'Large', 'type': 'fiend', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

