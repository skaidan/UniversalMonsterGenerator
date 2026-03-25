# bases1/fire-giant-forgecaller.py
"""
FireGiantForgecaller creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fire-giant-forgecaller
"""
from creature_base import GlobalCreatureBaseClass


class FireGiantForgecaller(GlobalCreatureBaseClass):
    """
    Huge Giant (Cleric) creature - FireGiantForgecaller
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 312, 'min_level': 1, 'level': 1, 'STR': 25, 'DEX': 11, 'CON': 23, 'INT': 16, 'WIS': 21, 'CHAR': 18, 'armor_class': 18, 'alignment': 'any alignment Armor Class  18 (plate) Hit Points  312 (25d12 + 150) Speed  30 ft.', 'legendary': False, 'size': 'Huge', 'type': 'Giant (Cleric)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

