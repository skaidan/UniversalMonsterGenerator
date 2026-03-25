# bases1/giant-ox.py
"""
GiantOx creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-ox
"""
from creature_base import GlobalCreatureBaseClass


class GiantOx(GlobalCreatureBaseClass):
    """
    Huge Fey creature - GiantOx
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 105, 'min_level': 1, 'level': 1, 'STR': 22, 'DEX': 10, 'CON': 19, 'INT': 4, 'WIS': 11, 'CHAR': 9, 'armor_class': 12, 'alignment': "unaligned Armor Class  12 (natural armor) Hit Points  105 (10d12 + 40) Speed  40 ft. STR 22 (+6) DEX 10 (+0) CON 19 (+4) INT 4 (-3) WIS 11 (+0) CHA 9 (-1) Senses  passive Perception 10 Languages  understands Giant and Sylvan but can't speak Challenge  3 (700 XP) \xa0 \xa0  Proficiency Bonus  +2 Beast of Burden. Actions Gore.", 'legendary': False, 'size': 'Huge', 'type': 'Fey', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

