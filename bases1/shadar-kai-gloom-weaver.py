# bases1/shadar-kai-gloom-weaver.py
"""
ShadarKaiGloomWeaver creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=shadar-kai-gloom-weaver
"""
from creature_base import GlobalCreatureBaseClass


class ShadarKaiGloomWeaver(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Elf) creature - ShadarKaiGloomWeaver
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 104, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 18, 'CON': 14, 'INT': 15, 'WIS': 12, 'CHAR': 18, 'armor_class': 14, 'alignment': 'typically Neutral Evil Armor Class  14 Hit Points  104 (16d8 + 32) Speed  30 ft. STR 11 (+0) DEX 18 (+4) CON 14 (+2) INT 15 (+2) WIS 12 (+1) CHA 18 (+4) Saving Throws  Dex +8', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Elf)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

