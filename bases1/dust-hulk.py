# bases1/dust-hulk.py
"""
DustHulk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dust-hulk
"""
from creature_base import GlobalCreatureBaseClass


class DustHulk(GlobalCreatureBaseClass):
    """
    Large Elemental creature - DustHulk
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 68, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 19, 'CON': 16, 'INT': 10, 'WIS': 12, 'CHAR': 8, 'armor_class': 16, 'alignment': 'typically Chaotic Neutral Armor Class  16 (natural armor) Hit Points  68 (8d10 + 24) Speed  0 ft.', 'legendary': False, 'size': 'Large', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

