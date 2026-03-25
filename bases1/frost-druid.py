# bases1/frost-druid.py
"""
FrostDruid creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=frost-druid
"""
from creature_base import GlobalCreatureBaseClass


class FrostDruid(GlobalCreatureBaseClass):
    """
    Medium humanoid (Human) creature - FrostDruid
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 67, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 13, 'CON': 16, 'INT': 10, 'WIS': 16, 'CHAR': 9, 'armor_class': 13, 'alignment': 'any alignment Armor Class  13 (hide armor) Hit Points  67 (9d8 + 27) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Human)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

