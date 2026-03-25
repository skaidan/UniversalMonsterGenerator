# bases1/tabaxi-minstrel.py
"""
TabaxiMinstrel creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=tabaxi-minstrel
"""
from creature_base import GlobalCreatureBaseClass


class TabaxiMinstrel(GlobalCreatureBaseClass):
    """
    Medium humanoid (Tabaxi) creature - TabaxiMinstrel
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 15, 'CON': 11, 'INT': 14, 'WIS': 12, 'CHAR': 16, 'armor_class': 12, 'alignment': 'chaotic good Armor Class  12 Hit Points  22 (5d8) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Tabaxi)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

