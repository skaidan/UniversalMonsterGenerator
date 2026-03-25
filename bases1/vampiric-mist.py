# bases1/vampiric-mist.py
"""
VampiricMist creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=vampiric-mist
"""
from creature_base import GlobalCreatureBaseClass


class VampiricMist(GlobalCreatureBaseClass):
    """
    Medium Undead creature - VampiricMist
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 30, 'min_level': 1, 'level': 1, 'STR': 6, 'DEX': 16, 'CON': 16, 'INT': 6, 'WIS': 12, 'CHAR': 7, 'armor_class': 13, 'alignment': 'typically Chaotic Evil Armor Class  13 Hit Points  30 (4d8 + 12) Speed  0 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

