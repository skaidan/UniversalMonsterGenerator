# bases1/fist-of-bane.py
"""
FistOfBane creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fist-of-bane
"""
from creature_base import GlobalCreatureBaseClass


class FistOfBane(GlobalCreatureBaseClass):
    """
    Medium humanoid (Human) creature - FistOfBane
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 11, 'CON': 13, 'INT': 10, 'WIS': 12, 'CHAR': 11, 'armor_class': 18, 'alignment': 'lawful evil Armor Class  18 (chain mail', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Human)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

