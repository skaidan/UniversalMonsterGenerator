# bases1/seal.py
"""
Seal creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=seal
"""
from creature_base import GlobalCreatureBaseClass


class Seal(GlobalCreatureBaseClass):
    """
    Medium beast creature - Seal
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 9, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 12, 'CON': 11, 'INT': 3, 'WIS': 12, 'CHAR': 5, 'armor_class': 11, 'alignment': 'unaligned Armor Class  11 Hit Points  9 (2d8) Speed  20 ft.', 'legendary': False, 'size': 'Medium', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

