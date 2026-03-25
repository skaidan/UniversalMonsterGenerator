# bases1/wersten-kern.py
"""
WerstenKern creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=wersten-kern
"""
from creature_base import GlobalCreatureBaseClass


class WerstenKern(GlobalCreatureBaseClass):
    """
    Medium Undead creature - WerstenKern
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 178, 'min_level': 1, 'level': 1, 'STR': 21, 'DEX': 10, 'CON': 18, 'INT': 13, 'WIS': 14, 'CHAR': 16, 'armor_class': 18, 'alignment': 'Lawful Evil Armor Class  18 (plate) Hit Points  178 (21d8 + 84) Speed  30 ft. STR 21 (+5) DEX 10 (+0) CON 18 (+4) INT 13 (+1) WIS 14 (+2) CHA 16 (+3) Saving Throws  Con +9', 'legendary': False, 'size': 'Medium', 'type': 'Undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

