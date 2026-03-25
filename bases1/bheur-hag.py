# bases1/bheur-hag.py
"""
BheurHag creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bheur-hag
"""
from creature_base import GlobalCreatureBaseClass


class BheurHag(GlobalCreatureBaseClass):
    """
    Medium Fey creature - BheurHag
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 91, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 16, 'CON': 14, 'INT': 12, 'WIS': 13, 'CHAR': 16, 'armor_class': 17, 'alignment': 'typically Chaotic Evil Armor Class  17 (natural armor) Hit Points  91 (14d8 + 28) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Fey', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

