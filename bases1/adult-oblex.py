# bases1/adult-oblex.py
"""
AdultOblex creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=adult-oblex
"""
from creature_base import GlobalCreatureBaseClass


class AdultOblex(GlobalCreatureBaseClass):
    """
    Medium Ooze creature - AdultOblex
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 75, 'min_level': 1, 'level': 1, 'STR': 8, 'DEX': 19, 'CON': 16, 'INT': 19, 'WIS': 12, 'CHAR': 15, 'armor_class': 14, 'alignment': 'typically Lawful Evil Armor Class  14 Hit Points  75 (10d8 + 30) Speed  20 ft. STR 8 (-1) DEX 19 (+4) CON 16 (+3) INT 19 (+4) WIS 12 (+1) CHA 15 (+2) Saving Throws  Int +7', 'legendary': False, 'size': 'Medium', 'type': 'Ooze', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

