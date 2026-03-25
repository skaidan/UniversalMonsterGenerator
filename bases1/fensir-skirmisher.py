# bases1/fensir-skirmisher.py
"""
FensirSkirmisher creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fensir-skirmisher
"""
from creature_base import GlobalCreatureBaseClass


class FensirSkirmisher(GlobalCreatureBaseClass):
    """
    Large Giant creature - FensirSkirmisher
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 94, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 15, 'CON': 20, 'INT': 14, 'WIS': 11, 'CHAR': 12, 'armor_class': 15, 'alignment': 'any alignment Armor Class  15 (chain shirt) Hit Points  94 (9d10 + 45) Speed  30 ft. STR 18 (+4) DEX 15 (+2) CON 20 (+5) INT 14 (+2) WIS 11 (+0) CHA 12 (+1) Saving Throws  Int +5', 'legendary': False, 'size': 'Large', 'type': 'Giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

