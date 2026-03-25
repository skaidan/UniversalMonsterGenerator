# bases1/dragonborn-of-sardior.py
"""
DragonbornOfSardior creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dragonborn-of-sardior
"""
from creature_base import GlobalCreatureBaseClass


class DragonbornOfSardior(GlobalCreatureBaseClass):
    """
    Medium humanoid creature - DragonbornOfSardior
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 75, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 16, 'CON': 17, 'INT': 18, 'WIS': 14, 'CHAR': 12, 'armor_class': 20, 'alignment': 'typically Neutral Armor Class  20 (mental defense) Hit Points  75 (10d8 + 30) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

