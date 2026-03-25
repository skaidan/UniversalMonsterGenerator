# bases1/olhydra.py
"""
Olhydra creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=olhydra
"""
from creature_base import GlobalCreatureBaseClass


class Olhydra(GlobalCreatureBaseClass):
    """
    Huge elemental creature - Olhydra
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 324, 'min_level': 1, 'level': 1, 'STR': 21, 'DEX': 22, 'CON': 24, 'INT': 17, 'WIS': 18, 'CHAR': 23, 'armor_class': 18, 'alignment': 'neutral evil Armor Class  18 (natural armor) Hit Points  324 (24d12 + 168) Speed  50 ft.', 'legendary': False, 'size': 'Huge', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

