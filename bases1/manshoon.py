# bases1/manshoon.py
"""
Manshoon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=manshoon
"""
from creature_base import GlobalCreatureBaseClass


class Manshoon(GlobalCreatureBaseClass):
    """
    Medium humanoid (Human) creature - Manshoon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 126, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 14, 'CON': 12, 'INT': 23, 'WIS': 15, 'CHAR': 16, 'armor_class': 19, 'alignment': 'lawful evil Armor Class  19 ( robe of the arch magi', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Human)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

