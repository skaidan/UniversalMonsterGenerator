# bases1/vellynne-harpell.py
"""
VellynneHarpell creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=vellynne-harpell
"""
from creature_base import GlobalCreatureBaseClass


class VellynneHarpell(GlobalCreatureBaseClass):
    """
    Medium humanoid (Human) creature - VellynneHarpell
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 67, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 12, 'CON': 17, 'INT': 18, 'WIS': 15, 'CHAR': 13, 'armor_class': 13, 'alignment': 'neutral Armor Class  13 ( bracers of defense ) Hit Points  67 (9d8 + 27) Speed  20 ft. STR 10 (+0) DEX 12 (+1) CON 17 (+3) INT 18 (+4) WIS 15 (+2) CHA 13 (+1) Saving Throws  Int +6', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Human)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

