# bases1/reaper-of-bhaal.py
"""
ReaperOfBhaal creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=reaper-of-bhaal
"""
from creature_base import GlobalCreatureBaseClass


class ReaperOfBhaal(GlobalCreatureBaseClass):
    """
    Medium humanoid (Human) creature - ReaperOfBhaal
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 27, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 20, 'CON': 13, 'INT': 15, 'WIS': 12, 'CHAR': 16, 'armor_class': 15, 'alignment': 'chaotic evil Armor Class  15 Hit Points  27 (5d8 + 5) Speed  40 ft. STR 11 (+0) DEX 20 (+5) CON 13 (+1) INT 15 (+2) WIS 12 (+1) CHA 16 (+3) Skills  Intimidation +5', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Human)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

