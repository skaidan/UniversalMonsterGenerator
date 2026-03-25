# bases1/shadar-kai-soul-monger.py
"""
ShadarKaiSoulMonger creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=shadar-kai-soul-monger
"""
from creature_base import GlobalCreatureBaseClass


class ShadarKaiSoulMonger(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Elf) creature - ShadarKaiSoulMonger
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 136, 'min_level': 1, 'level': 1, 'STR': 8, 'DEX': 17, 'CON': 14, 'INT': 19, 'WIS': 15, 'CHAR': 13, 'armor_class': 15, 'alignment': 'typically Neutral Evil Armor Class  15 (studded leather) Hit Points  136 (21d8 + 42) Speed  30 ft. STR 8 (-1) DEX 17 (+3) CON 14 (+2) INT 19 (+4) WIS 15 (+2) CHA 13 (+1) Saving Throws  Dex +7', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Elf)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

