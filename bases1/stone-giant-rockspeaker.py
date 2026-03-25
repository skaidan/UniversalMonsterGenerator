# bases1/stone-giant-rockspeaker.py
"""
StoneGiantRockspeaker creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=stone-giant-rockspeaker
"""
from creature_base import GlobalCreatureBaseClass


class StoneGiantRockspeaker(GlobalCreatureBaseClass):
    """
    Huge Giant (Wizard) creature - StoneGiantRockspeaker
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 276, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 15, 'CON': 20, 'INT': 19, 'WIS': 14, 'CHAR': 10, 'armor_class': 19, 'alignment': 'any alignment Armor Class  19 (natural armor) Hit Points  276 (24d12 + 120) Speed  40 ft. STR 23 (+6) DEX 15 (+2) CON 20 (+5) INT 19 (+4) WIS 14 (+2) CHA 10 (+0) Saving Throws  Dex +7', 'legendary': False, 'size': 'Huge', 'type': 'Giant (Wizard)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

