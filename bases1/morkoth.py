# bases1/morkoth.py
"""
Morkoth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=morkoth
"""
from creature_base import GlobalCreatureBaseClass


class Morkoth(GlobalCreatureBaseClass):
    """
    Large Aberration creature - Morkoth
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 165, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 14, 'CON': 14, 'INT': 20, 'WIS': 15, 'CHAR': 13, 'armor_class': 17, 'alignment': 'typically Chaotic Evil Armor Class  17 (natural armor) Hit Points  165 (22d10 + 44) Speed  25 ft.', 'legendary': False, 'size': 'Large', 'type': 'Aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

