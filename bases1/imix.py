# bases1/imix.py
"""
Imix creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=imix
"""
from creature_base import GlobalCreatureBaseClass


class Imix(GlobalCreatureBaseClass):
    """
    Huge elemental creature - Imix
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 325, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 24, 'CON': 22, 'INT': 15, 'WIS': 16, 'CHAR': 23, 'armor_class': 17, 'alignment': 'neutral evil Armor Class  17 Hit Points  325 (26d12 + 156) Speed  50 ft.', 'legendary': False, 'size': 'Huge', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

