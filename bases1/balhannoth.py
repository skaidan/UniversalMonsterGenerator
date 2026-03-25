# bases1/balhannoth.py
"""
Balhannoth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=balhannoth
"""
from creature_base import GlobalCreatureBaseClass


class Balhannoth(GlobalCreatureBaseClass):
    """
    Large Aberration creature - Balhannoth
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 114, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 8, 'CON': 18, 'INT': 6, 'WIS': 15, 'CHAR': 8, 'armor_class': 17, 'alignment': 'typically Chaotic Evil Armor Class  17 (natural armor) Hit Points  114 (12d10 + 48) Speed  25 ft.', 'legendary': False, 'size': 'Large', 'type': 'Aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

