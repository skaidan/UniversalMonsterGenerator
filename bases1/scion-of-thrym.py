# bases1/scion-of-thrym.py
"""
ScionOfThrym creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=scion-of-thrym
"""
from creature_base import GlobalCreatureBaseClass


class ScionOfThrym(GlobalCreatureBaseClass):
    """
    Gargantuan Giant (Titan) creature - ScionOfThrym
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 499, 'min_level': 1, 'level': 1, 'STR': 30, 'DEX': 16, 'CON': 27, 'INT': 17, 'WIS': 20, 'CHAR': 21, 'armor_class': 19, 'alignment': 'typically Neutral Evil Armor Class  19 (natural armor) Hit Points  499 (27d20 + 216) Speed  60 ft. STR 30 (+10) DEX 16 (+3) CON 27 (+8) INT 17 (+3) WIS 20 (+5) CHA 21 (+5) Saving Throws  Wis +12', 'legendary': False, 'size': 'Gargantuan', 'type': 'Giant (Titan)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

