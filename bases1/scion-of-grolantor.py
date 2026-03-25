# bases1/scion-of-grolantor.py
"""
ScionOfGrolantor creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=scion-of-grolantor
"""
from creature_base import GlobalCreatureBaseClass


class ScionOfGrolantor(GlobalCreatureBaseClass):
    """
    Gargantuan Giant (Titan) creature - ScionOfGrolantor
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 402, 'min_level': 1, 'level': 1, 'STR': 27, 'DEX': 14, 'CON': 25, 'INT': 15, 'WIS': 21, 'CHAR': 18, 'armor_class': 18, 'alignment': 'typically Chaotic Evil Armor Class  18 (natural armor) Hit Points  402 (23d20 + 161) Speed  60 ft. STR 27 (+8) DEX 14 (+2) CON 25 (+7) INT 15 (+2) WIS 21 (+5) CHA 18 (+4) Saving Throws  Wis +12', 'legendary': False, 'size': 'Gargantuan', 'type': 'Giant (Titan)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

