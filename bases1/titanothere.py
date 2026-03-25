# bases1/titanothere.py
"""
Titanothere creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=titanothere
"""
from creature_base import GlobalCreatureBaseClass


class Titanothere(GlobalCreatureBaseClass):
    """
    Huge Beast creature - Titanothere
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 136, 'min_level': 1, 'level': 1, 'STR': 25, 'DEX': 10, 'CON': 19, 'INT': 2, 'WIS': 12, 'CHAR': 6, 'armor_class': 16, 'alignment': 'unaligned Armor Class  16 (natural armor) Hit Points  136 (13d12 + 52) Speed  50 ft. STR 25 (+7) DEX 10 (+0) CON 19 (+4) INT 2 (-4) WIS 12 (+1) CHA 6 (-2) Senses  passive Perception 11 Languages  — Challenge  5 (1800 XP) \xa0 \xa0  Proficiency Bonus  +3 Beast of Burden. Actions Stomp.', 'legendary': False, 'size': 'Huge', 'type': 'Beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

