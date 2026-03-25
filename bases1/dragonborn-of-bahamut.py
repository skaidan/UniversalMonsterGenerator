# bases1/dragonborn-of-bahamut.py
"""
DragonbornOfBahamut creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dragonborn-of-bahamut
"""
from creature_base import GlobalCreatureBaseClass


class DragonbornOfBahamut(GlobalCreatureBaseClass):
    """
    Medium humanoid creature - DragonbornOfBahamut
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 93, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 13, 'CON': 18, 'INT': 12, 'WIS': 14, 'CHAR': 17, 'armor_class': 18, 'alignment': 'typically Lawful Good Armor Class  18 (half plate', 'legendary': False, 'size': 'Medium', 'type': 'humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

