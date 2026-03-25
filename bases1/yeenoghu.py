# bases1/yeenoghu.py
"""
Yeenoghu creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yeenoghu
"""
from creature_base import GlobalCreatureBaseClass


class Yeenoghu(GlobalCreatureBaseClass):
    """
    Huge Fiend (Demon) creature - Yeenoghu
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 333, 'min_level': 1, 'level': 1, 'STR': 29, 'DEX': 16, 'CON': 23, 'INT': 15, 'WIS': 24, 'CHAR': 15, 'armor_class': 20, 'alignment': 'Chaotic Evil Armor Class  20 (natural armor) Hit Points  333 (23d12 + 184) Speed  50 ft. STR 29 (+9) DEX 16 (+3) CON 23 (+6) INT 15 (+2) WIS 24 (+7) CHA 15 (+2) Saving Throws  Dex +10', 'legendary': False, 'size': 'Huge', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

