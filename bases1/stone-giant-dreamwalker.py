# bases1/stone-giant-dreamwalker.py
"""
StoneGiantDreamwalker creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=stone-giant-dreamwalker
"""
from creature_base import GlobalCreatureBaseClass


class StoneGiantDreamwalker(GlobalCreatureBaseClass):
    """
    Huge Giant creature - StoneGiantDreamwalker
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 161, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 14, 'CON': 21, 'INT': 10, 'WIS': 8, 'CHAR': 12, 'armor_class': 18, 'alignment': 'typically Chaotic Neutral Armor Class  18 (natural armor) Hit Points  161 (14d12 + 70) Speed  40 ft. STR 23 (+6) DEX 14 (+2) CON 21 (+5) INT 10 (+0) WIS 8 (-1) CHA 12 (+1) Saving Throws  Dex +6', 'legendary': False, 'size': 'Huge', 'type': 'Giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

