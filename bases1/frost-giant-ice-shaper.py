# bases1/frost-giant-ice-shaper.py
"""
FrostGiantIceShaper creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=frost-giant-ice-shaper
"""
from creature_base import GlobalCreatureBaseClass


class FrostGiantIceShaper(GlobalCreatureBaseClass):
    """
    Huge Giant (Cleric) creature - FrostGiantIceShaper
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 310, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 10, 'CON': 21, 'INT': 11, 'WIS': 19, 'CHAR': 16, 'armor_class': 16, 'alignment': 'any alignment Armor Class  16 (chain mail) Hit Points  310 (27d12 + 135) Speed  40 ft. STR 23 (+6) DEX 10 (+0) CON 21 (+5) INT 11 (+0) WIS 19 (+4) CHA 16 (+3) Saving Throws  Str +12', 'legendary': False, 'size': 'Huge', 'type': 'Giant (Cleric)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

