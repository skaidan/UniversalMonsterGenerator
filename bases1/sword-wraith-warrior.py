# bases1/sword-wraith-warrior.py
"""
SwordWraithWarrior creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=sword-wraith-warrior
"""
from creature_base import GlobalCreatureBaseClass


class SwordWraithWarrior(GlobalCreatureBaseClass):
    """
    Medium Undead creature - SwordWraithWarrior
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 45, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 12, 'CON': 17, 'INT': 6, 'WIS': 9, 'CHAR': 10, 'armor_class': 16, 'alignment': 'typically Lawful Evil Armor Class  16 (chain shirt', 'legendary': False, 'size': 'Medium', 'type': 'Undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

