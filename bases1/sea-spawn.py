# bases1/sea-spawn.py
"""
SeaSpawn creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=sea-spawn
"""
from creature_base import GlobalCreatureBaseClass


class SeaSpawn(GlobalCreatureBaseClass):
    """
    Medium Monstrosity creature - SeaSpawn
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 32, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 8, 'CON': 15, 'INT': 6, 'WIS': 10, 'CHAR': 8, 'armor_class': 11, 'alignment': 'typically Neutral Evil Armor Class  11 (natural armor) Hit Points  32 (5d8 + 10) Speed  20 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

