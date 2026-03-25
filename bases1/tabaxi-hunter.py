# bases1/tabaxi-hunter.py
"""
TabaxiHunter creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=tabaxi-hunter
"""
from creature_base import GlobalCreatureBaseClass


class TabaxiHunter(GlobalCreatureBaseClass):
    """
    Medium humanoid (Tabaxi) creature - TabaxiHunter
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 40, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 17, 'CON': 11, 'INT': 13, 'WIS': 14, 'CHAR': 15, 'armor_class': 14, 'alignment': 'chaotic good Armor Class  14 (leather armor) Hit Points  40 (9d8) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Tabaxi)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

