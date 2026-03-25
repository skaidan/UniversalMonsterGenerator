# bases1/elder-oblex.py
"""
ElderOblex creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=elder-oblex
"""
from creature_base import GlobalCreatureBaseClass


class ElderOblex(GlobalCreatureBaseClass):
    """
    Huge Ooze creature - ElderOblex
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 115, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 16, 'CON': 21, 'INT': 22, 'WIS': 13, 'CHAR': 18, 'armor_class': 16, 'alignment': 'typically Lawful Evil Armor Class  16 Hit Points  115 (10d12 + 50) Speed  20 ft. STR 15 (+2) DEX 16 (+3) CON 21 (+5) INT 22 (+6) WIS 13 (+1) CHA 18 (+4) Saving Throws  Int +10', 'legendary': False, 'size': 'Huge', 'type': 'Ooze', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

