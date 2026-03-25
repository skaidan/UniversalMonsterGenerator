# bases1/barrowghast.py
"""
Barrowghast creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=barrowghast
"""
from creature_base import GlobalCreatureBaseClass


class Barrowghast(GlobalCreatureBaseClass):
    """
    Huge Undead creature - Barrowghast
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 138, 'min_level': 1, 'level': 1, 'STR': 21, 'DEX': 8, 'CON': 20, 'INT': 5, 'WIS': 9, 'CHAR': 6, 'armor_class': 12, 'alignment': 'typically Chaotic Evil Armor Class  12 (natural armor) Hit Points  138 (12d12 + 60) Speed  40 ft. STR 21 (+5) DEX 8 (-1) CON 20 (+5) INT 5 (-3) WIS 9 (-1) CHA 6 (-2) Damage Resistances  necrotic', 'legendary': False, 'size': 'Huge', 'type': 'Undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

