# bases1/miirym.py
"""
Miirym creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=miirym
"""
from creature_base import GlobalCreatureBaseClass


class Miirym(GlobalCreatureBaseClass):
    """
    Large undead creature - Miirym
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 262, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 10, 'CON': 20, 'INT': 18, 'WIS': 15, 'CHAR': 23, 'armor_class': 10, 'alignment': '- Armor Class  10 Hit Points  262 (25d10 + 125) Speed  0 ft.', 'legendary': False, 'size': 'Large', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

