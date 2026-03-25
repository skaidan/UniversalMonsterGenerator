# bases1/mouth-of-grolantor.py
"""
MouthOfGrolantor creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mouth-of-grolantor
"""
from creature_base import GlobalCreatureBaseClass


class MouthOfGrolantor(GlobalCreatureBaseClass):
    """
    Huge Giant creature - MouthOfGrolantor
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 105, 'min_level': 1, 'level': 1, 'STR': 21, 'DEX': 10, 'CON': 18, 'INT': 5, 'WIS': 7, 'CHAR': 5, 'armor_class': 14, 'alignment': 'typically Chaotic Evil Armor Class  14 (natural armor) Hit Points  105 (10d12 + 40) Speed  50 ft. STR 21 (+5) DEX 10 (+0) CON 18 (+4) INT 5 (-3) WIS 7 (-2) CHA 5 (-3) Skills  Perception +1 Condition Immunities  frightened Senses  passive Perception 11 Languages  Giant Challenge  6 (2300 XP) \xa0 \xa0  Proficiency Bonus  +3 Mouth of Chaos. Actions Bite. Fist.', 'legendary': False, 'size': 'Huge', 'type': 'Giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

