# bases1/frost-giant-everlasting-one.py
"""
FrostGiantEverlastingOne creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=frost-giant-everlasting-one
"""
from creature_base import GlobalCreatureBaseClass


class FrostGiantEverlastingOne(GlobalCreatureBaseClass):
    """
    Huge Giant creature - FrostGiantEverlastingOne
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 189, 'min_level': 1, 'level': 1, 'STR': 25, 'DEX': 9, 'CON': 24, 'INT': 9, 'WIS': 10, 'CHAR': 12, 'armor_class': 15, 'alignment': 'typically Chaotic Evil Armor Class  15 (patchwork armor) Hit Points  189 (14d12 + 98) Speed  40 ft. STR 25 (+7) DEX 9 (-1) CON 24 (+7) INT 9 (-1) WIS 10 (+0) CHA 12 (+1) Saving Throws  Str +11', 'legendary': False, 'size': 'Huge', 'type': 'Giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

