# bases1/hill-giant-avalancher.py
"""
HillGiantAvalancher creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hill-giant-avalancher
"""
from creature_base import GlobalCreatureBaseClass


class HillGiantAvalancher(GlobalCreatureBaseClass):
    """
    Huge Giant (Druid) creature - HillGiantAvalancher
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 220, 'min_level': 1, 'level': 1, 'STR': 21, 'DEX': 8, 'CON': 19, 'INT': 9, 'WIS': 18, 'CHAR': 10, 'armor_class': 15, 'alignment': 'any alignment Armor Class  15 (natural armor) Hit Points  220 (21d12 + 84) Speed  40 ft. STR 21 (+5) DEX 8 (-1) CON 19 (+4) INT 9 (-1) WIS 18 (+4) CHA 10 (+0) Saving Throws  Str +9', 'legendary': False, 'size': 'Huge', 'type': 'Giant (Druid)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

