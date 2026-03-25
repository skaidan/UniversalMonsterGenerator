# bases1/graz-zt.py
"""
GrazZt creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=graz-zt
"""
from creature_base import GlobalCreatureBaseClass


class GrazZt(GlobalCreatureBaseClass):
    """
    Large Fiend (Demon) creature - GrazZt
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 346, 'min_level': 1, 'level': 1, 'STR': 22, 'DEX': 15, 'CON': 21, 'INT': 23, 'WIS': 21, 'CHAR': 26, 'armor_class': 20, 'alignment': 'Chaotic Evil Armor Class  20 (natural armor) Hit Points  346 (33d10 + 165) Speed  40 ft. STR 22 (+6) DEX 15 (+2) CON 21 (+5) INT 23 (+6) WIS 21 (+5) CHA 26 (+8) Saving Throws  Dex +9', 'legendary': False, 'size': 'Large', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

