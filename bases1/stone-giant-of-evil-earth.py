# bases1/stone-giant-of-evil-earth.py
"""
StoneGiantOfEvilEarth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=stone-giant-of-evil-earth
"""
from creature_base import GlobalCreatureBaseClass


class StoneGiantOfEvilEarth(GlobalCreatureBaseClass):
    """
    Huge Giant creature - StoneGiantOfEvilEarth
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 137, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 13, 'CON': 22, 'INT': 10, 'WIS': 12, 'CHAR': 9, 'armor_class': 20, 'alignment': 'typically Neutral Evil Armor Class  20 (plate) Hit Points  137 (11d12 + 66) Speed  40 ft. STR 23 (+6) DEX 13 (+1) CON 22 (+6) INT 10 (+0) WIS 12 (+1) CHA 9 (-1) Saving Throws  Str +10', 'legendary': False, 'size': 'Huge', 'type': 'Giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

