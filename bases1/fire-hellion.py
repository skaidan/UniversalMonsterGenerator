# bases1/fire-hellion.py
"""
FireHellion creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fire-hellion
"""
from creature_base import GlobalCreatureBaseClass


class FireHellion(GlobalCreatureBaseClass):
    """
    Huge Fiend (Devil) creature - FireHellion
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 175, 'min_level': 1, 'level': 1, 'STR': 25, 'DEX': 10, 'CON': 23, 'INT': 16, 'WIS': 14, 'CHAR': 21, 'armor_class': 18, 'alignment': 'typically Lawful Evil Armor Class  18 (plate) Hit Points  175 (14d12 + 84) Speed  30 ft. STR 25 (+7) DEX 10 (+0) CON 23 (+6) INT 16 (+3) WIS 14 (+2) CHA 21 (+5) Saving Throws  Wis +6', 'legendary': False, 'size': 'Huge', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

