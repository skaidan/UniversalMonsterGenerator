# bases1/cairnwight.py
"""
Cairnwight creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cairnwight
"""
from creature_base import GlobalCreatureBaseClass


class Cairnwight(GlobalCreatureBaseClass):
    """
    Huge Undead creature - Cairnwight
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 138, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 10, 'CON': 21, 'INT': 10, 'WIS': 12, 'CHAR': 9, 'armor_class': 19, 'alignment': 'typically Neutral Armor Class  19 (natural armor) Hit Points  138 (12d12 + 60) Speed  40 ft. STR 23 (+6) DEX 10 (+0) CON 21 (+5) INT 10 (+0) WIS 12 (+1) CHA 9 (-1) Saving Throws  Con +9', 'legendary': False, 'size': 'Huge', 'type': 'Undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

