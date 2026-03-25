# bases1/vajra-safahr.py
"""
VajraSafahr creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=vajra-safahr
"""
from creature_base import GlobalCreatureBaseClass


class VajraSafahr(GlobalCreatureBaseClass):
    """
    Medium humanoid (Human) creature - VajraSafahr
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 126, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 14, 'CON': 12, 'INT': 20, 'WIS': 11, 'CHAR': 16, 'armor_class': 14, 'alignment': 'lawful neutral Armor Class  14 ( Blackstaff ; 17 with  mage armor ) Hit Points  126 (23d8 + 23) Speed  30 ft. STR 10 (+0) DEX 14 (+2) CON 12 (+1) INT 20 (+5) WIS 11 (+0) CHA 16 (+3) Saving Throws  Str +2', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Human)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

