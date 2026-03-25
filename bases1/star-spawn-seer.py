# bases1/star-spawn-seer.py
"""
StarSpawnSeer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=star-spawn-seer
"""
from creature_base import GlobalCreatureBaseClass


class StarSpawnSeer(GlobalCreatureBaseClass):
    """
    Medium Aberration creature - StarSpawnSeer
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 153, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 12, 'CON': 18, 'INT': 22, 'WIS': 19, 'CHAR': 16, 'armor_class': 17, 'alignment': 'typically Neutral Evil Armor Class  17 (natural armor) Hit Points  153 (18d8 + 72) Speed  30 ft. STR 14 (+2) DEX 12 (+1) CON 18 (+4) INT 22 (+6) WIS 19 (+4) CHA 16 (+3) Saving Throws  Dex +6', 'legendary': False, 'size': 'Medium', 'type': 'Aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

