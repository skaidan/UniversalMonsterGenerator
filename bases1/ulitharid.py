# bases1/ulitharid.py
"""
Ulitharid creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ulitharid
"""
from creature_base import GlobalCreatureBaseClass


class Ulitharid(GlobalCreatureBaseClass):
    """
    Large Aberration (Mind Flayer) creature - Ulitharid
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 127, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 12, 'CON': 15, 'INT': 21, 'WIS': 19, 'CHAR': 21, 'armor_class': 15, 'alignment': 'typically Lawful Evil Armor Class  15 (breastplate) Hit Points  127 (17d10 + 34) Speed  30 ft. STR 15 (+2) DEX 12 (+1) CON 15 (+2) INT 21 (+5) WIS 19 (+4) CHA 21 (+5) Saving Throws  Int +9', 'legendary': False, 'size': 'Large', 'type': 'Aberration (Mind Flayer)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

