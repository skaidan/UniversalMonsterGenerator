# bases1/ghost-dragon.py
"""
GhostDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ghost-dragon
"""
from creature_base import GlobalCreatureBaseClass


class GhostDragon(GlobalCreatureBaseClass):
    """
    Huge undead creature - GhostDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 324, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 10, 'CON': 25, 'INT': 16, 'WIS': 15, 'CHAR': 19, 'armor_class': 10, 'alignment': 'any alignment Armor Class  10 Hit Points  324 (24d12 + 168) Speed  40 ft.', 'legendary': False, 'size': 'Huge', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

