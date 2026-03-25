# bases1/yan-c-bin.py
"""
YanCBin creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yan-c-bin
"""
from creature_base import GlobalCreatureBaseClass


class YanCBin(GlobalCreatureBaseClass):
    """
    Huge elemental creature - YanCBin
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 283, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 24, 'CON': 24, 'INT': 16, 'WIS': 21, 'CHAR': 23, 'armor_class': 22, 'alignment': 'neutral evil Armor Class  22 (natural armor) Hit Points  283 (21d12 + 147) Speed  50 ft.', 'legendary': False, 'size': 'Huge', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

