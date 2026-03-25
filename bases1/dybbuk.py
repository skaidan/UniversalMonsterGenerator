# bases1/dybbuk.py
"""
Dybbuk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dybbuk
"""
from creature_base import GlobalCreatureBaseClass


class Dybbuk(GlobalCreatureBaseClass):
    """
    Medium Fiend (Demon) creature - Dybbuk
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 37, 'min_level': 1, 'level': 1, 'STR': 6, 'DEX': 19, 'CON': 16, 'INT': 16, 'WIS': 15, 'CHAR': 14, 'armor_class': 14, 'alignment': 'typically Chaotic Evil Armor Class  14 Hit Points  37 (5d8 + 15) Speed  40 ft. (hover) STR 6 (-2) DEX 19 (+4) CON 16 (+3) INT 16 (+3) WIS 15 (+2) CHA 14 (+2) Skills  Deception +6', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

