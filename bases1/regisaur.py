# bases1/regisaur.py
"""
Regisaur creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=regisaur
"""
from creature_base import GlobalCreatureBaseClass


class Regisaur(GlobalCreatureBaseClass):
    """
    Gargantuan Monstrosity (Dinosaur) creature - Regisaur
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 181, 'min_level': 1, 'level': 1, 'STR': 27, 'DEX': 8, 'CON': 23, 'INT': 4, 'WIS': 12, 'CHAR': 6, 'armor_class': 17, 'alignment': 'unaligned Armor Class  17 (natural armor) Hit Points  181 (11d20 + 66) Speed  40 ft. STR 27 (+8) DEX 8 (-1) CON 23 (+6) INT 4 (-3) WIS 12 (+1) CHA 6 (-2) Senses  passive Perception 11 Languages  — Challenge  14 (11500 XP) \xa0 \xa0  Proficiency Bonus  +5 Magic Resistance. Actions Multiattack. Bite. Tail. Bonus actions Swallow.', 'legendary': False, 'size': 'Gargantuan', 'type': 'Monstrosity (Dinosaur)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

