# bases1/maw-of-yeenoghu.py
"""
MawOfYeenoghu creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=maw-of-yeenoghu
"""
from creature_base import GlobalCreatureBaseClass


class MawOfYeenoghu(GlobalCreatureBaseClass):
    """
    Huge Fiend (Demon) creature - MawOfYeenoghu
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 161, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 10, 'CON': 21, 'INT': 8, 'WIS': 14, 'CHAR': 10, 'armor_class': 15, 'alignment': 'typically Chaotic Evil Armor Class  15 (natural armor) Hit Points  161 (14d12 + 70) Speed  40 ft. STR 23 (+6) DEX 10 (+0) CON 21 (+5) INT 8 (-1) WIS 14 (+2) CHA 10 (+0) Saving Throws  Con +9', 'legendary': False, 'size': 'Huge', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

