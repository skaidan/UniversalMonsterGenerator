# bases1/dire-troll.py
"""
DireTroll creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dire-troll
"""
from creature_base import GlobalCreatureBaseClass


class DireTroll(GlobalCreatureBaseClass):
    """
    Huge Giant creature - DireTroll
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 172, 'min_level': 1, 'level': 1, 'STR': 22, 'DEX': 15, 'CON': 21, 'INT': 9, 'WIS': 11, 'CHAR': 5, 'armor_class': 15, 'alignment': 'typically Chaotic Evil Armor Class  15 (natural armor) Hit Points  172 (15d12 + 75) Speed  40 ft. STR 22 (+6) DEX 15 (+2) CON 21 (+5) INT 9 (-1) WIS 11 (+0) CHA 5 (-3) Saving Throws  Wis +5', 'legendary': False, 'size': 'Huge', 'type': 'Giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

