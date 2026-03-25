# bases1/tempest-spirit.py
"""
TempestSpirit creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=tempest-spirit
"""
from creature_base import GlobalCreatureBaseClass


class TempestSpirit(GlobalCreatureBaseClass):
    """
    Huge Undead creature - TempestSpirit
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 195, 'min_level': 1, 'level': 1, 'STR': 24, 'DEX': 14, 'CON': 20, 'INT': 16, 'WIS': 18, 'CHAR': 19, 'armor_class': 12, 'alignment': 'typically Chaotic Evil Armor Class  12 Hit Points  195 (17d12 + 85) Speed  0 ft.', 'legendary': False, 'size': 'Huge', 'type': 'Undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

