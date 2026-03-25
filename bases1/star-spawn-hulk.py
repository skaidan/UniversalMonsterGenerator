# bases1/star-spawn-hulk.py
"""
StarSpawnHulk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=star-spawn-hulk
"""
from creature_base import GlobalCreatureBaseClass


class StarSpawnHulk(GlobalCreatureBaseClass):
    """
    Large Aberration creature - StarSpawnHulk
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 136, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 8, 'CON': 21, 'INT': 7, 'WIS': 12, 'CHAR': 9, 'armor_class': 16, 'alignment': 'typically Chaotic Evil Armor Class  16 (natural armor) Hit Points  136 (13d10 + 65) Speed  30 ft. STR 20 (+5) DEX 8 (-1) CON 21 (+5) INT 7 (-2) WIS 12 (+1) CHA 9 (-1) Saving Throws  Dex +3', 'legendary': False, 'size': 'Large', 'type': 'Aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

