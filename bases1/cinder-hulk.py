# bases1/cinder-hulk.py
"""
CinderHulk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cinder-hulk
"""
from creature_base import GlobalCreatureBaseClass


class CinderHulk(GlobalCreatureBaseClass):
    """
    Large Elemental creature - CinderHulk
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 84, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 12, 'CON': 20, 'INT': 9, 'WIS': 14, 'CHAR': 10, 'armor_class': 16, 'alignment': 'typically Chaotic Evil Armor Class  16 (natural armor) Hit Points  84 (8d10 + 40) Speed  40 ft. STR 20 (+5) DEX 12 (+1) CON 20 (+5) INT 9 (-1) WIS 14 (+2) CHA 10 (+0) Saving Throws  Dex +4', 'legendary': False, 'size': 'Large', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

