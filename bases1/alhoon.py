# bases1/alhoon.py
"""
Alhoon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=alhoon
"""
from creature_base import GlobalCreatureBaseClass


class Alhoon(GlobalCreatureBaseClass):
    """
    Medium Undead (Mind Flayer creature - Alhoon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 150, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 12, 'CON': 16, 'INT': 19, 'WIS': 17, 'CHAR': 17, 'armor_class': 15, 'alignment': 'Wizard)', 'legendary': False, 'size': 'Medium', 'type': 'Undead (Mind Flayer', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

