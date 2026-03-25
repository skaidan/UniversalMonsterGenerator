# bases1/spotted-lion.py
"""
SpottedLion creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=spotted-lion
"""
from creature_base import GlobalCreatureBaseClass


class SpottedLion(GlobalCreatureBaseClass):
    """
    Huge Beast creature - SpottedLion
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 66, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 14, 'CON': 17, 'INT': 5, 'WIS': 13, 'CHAR': 10, 'armor_class': 15, 'alignment': 'unaligned Armor Class  15 (natural armor) Hit Points  66 (7d12 + 21) Speed  60 ft. STR 23 (+6) DEX 14 (+2) CON 17 (+3) INT 5 (-3) WIS 13 (+1) CHA 10 (+0) Skills  Perception +5', 'legendary': False, 'size': 'Huge', 'type': 'Beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

