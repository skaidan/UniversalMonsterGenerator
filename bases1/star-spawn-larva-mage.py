# bases1/star-spawn-larva-mage.py
"""
StarSpawnLarvaMage creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=star-spawn-larva-mage
"""
from creature_base import GlobalCreatureBaseClass


class StarSpawnLarvaMage(GlobalCreatureBaseClass):
    """
    Medium Aberration creature - StarSpawnLarvaMage
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 168, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 12, 'CON': 23, 'INT': 18, 'WIS': 12, 'CHAR': 16, 'armor_class': 16, 'alignment': 'typically Chaotic Evil Armor Class  16 (natural armor) Hit Points  168 (16d8 + 96) Speed  30 ft. STR 17 (+3) DEX 12 (+1) CON 23 (+6) INT 18 (+4) WIS 12 (+1) CHA 16 (+3) Saving Throws  Dex +6', 'legendary': False, 'size': 'Medium', 'type': 'Aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

