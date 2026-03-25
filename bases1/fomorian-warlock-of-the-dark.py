# bases1/fomorian-warlock-of-the-dark.py
"""
FomorianWarlockOfTheDark creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fomorian-warlock-of-the-dark
"""
from creature_base import GlobalCreatureBaseClass


class FomorianWarlockOfTheDark(GlobalCreatureBaseClass):
    """
    Huge Giant creature - FomorianWarlockOfTheDark
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 207, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 13, 'CON': 20, 'INT': 9, 'WIS': 14, 'CHAR': 18, 'armor_class': 15, 'alignment': 'any alignment Armor Class  15 (natural armor) Hit Points  207 (18d12 + 90) Speed  30 ft. STR 23 (+6) DEX 13 (+1) CON 20 (+5) INT 9 (-1) WIS 14 (+2) CHA 18 (+4) Saving Throws  Wis +6', 'legendary': False, 'size': 'Huge', 'type': 'Giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

