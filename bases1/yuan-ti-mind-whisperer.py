# bases1/yuan-ti-mind-whisperer.py
"""
YuanTiMindWhisperer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yuan-ti-mind-whisperer
"""
from creature_base import GlobalCreatureBaseClass


class YuanTiMindWhisperer(GlobalCreatureBaseClass):
    """
    Medium Monstrosity (Warlock) creature - YuanTiMindWhisperer
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 71, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 14, 'CON': 13, 'INT': 14, 'WIS': 14, 'CHAR': 16, 'armor_class': 14, 'alignment': 'typically Neutral Evil Armor Class  14 (natural armor) Hit Points  71 (13d8 + 13) Speed  30 ft. STR 16 (+3) DEX 14 (+2) CON 13 (+1) INT 14 (+2) WIS 14 (+2) CHA 16 (+3) Saving Throws  Wis +4', 'legendary': False, 'size': 'Medium', 'type': 'Monstrosity (Warlock)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

