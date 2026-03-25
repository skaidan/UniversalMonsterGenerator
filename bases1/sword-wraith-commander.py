# bases1/sword-wraith-commander.py
"""
SwordWraithCommander creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=sword-wraith-commander
"""
from creature_base import GlobalCreatureBaseClass


class SwordWraithCommander(GlobalCreatureBaseClass):
    """
    Medium Undead creature - SwordWraithCommander
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 127, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 14, 'CON': 18, 'INT': 11, 'WIS': 12, 'CHAR': 14, 'armor_class': 18, 'alignment': 'typically Lawful Evil Armor Class  18 (breastplate', 'legendary': False, 'size': 'Medium', 'type': 'Undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

