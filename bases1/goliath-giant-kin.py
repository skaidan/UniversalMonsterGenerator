# bases1/goliath-giant-kin.py
"""
GoliathGiantKin creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=goliath-giant-kin
"""
from creature_base import GlobalCreatureBaseClass


class GoliathGiantKin(GlobalCreatureBaseClass):
    """
    Medium Humanoid creature - GoliathGiantKin
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 67, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 13, 'CON': 16, 'INT': 10, 'WIS': 12, 'CHAR': 12, 'armor_class': 18, 'alignment': 'any alignment Armor Class  18 (half plate', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

