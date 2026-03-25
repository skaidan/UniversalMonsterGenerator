# bases1/aurochs.py
"""
Aurochs creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=aurochs
"""
from creature_base import GlobalCreatureBaseClass


class Aurochs(GlobalCreatureBaseClass):
    """
    Large Beast (Cattle) creature - Aurochs
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 38, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 10, 'CON': 19, 'INT': 2, 'WIS': 12, 'CHAR': 5, 'armor_class': 11, 'alignment': 'unaligned Armor Class  11 (natural armor) Hit Points  38 (4d10 + 16) Speed  50 ft. STR 20 (+5) DEX 10 (+0) CON 19 (+4) INT 2 (-4) WIS 12 (+1) CHA 5 (-3) Senses  passive Perception 11 Languages  — Challenge  2 (450 XP) \xa0 \xa0  Proficiency Bonus  +2 Actions Gore.', 'legendary': False, 'size': 'Large', 'type': 'Beast (Cattle)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

