# bases1/shadar-kai-shadow-dancer.py
"""
ShadarKaiShadowDancer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=shadar-kai-shadow-dancer
"""
from creature_base import GlobalCreatureBaseClass


class ShadarKaiShadowDancer(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Elf) creature - ShadarKaiShadowDancer
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 71, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 16, 'CON': 13, 'INT': 11, 'WIS': 12, 'CHAR': 12, 'armor_class': 15, 'alignment': 'any alignment Armor Class  15 (studded leather) Hit Points  71 (13d8 + 13) Speed  30 ft. STR 12 (+1) DEX 16 (+3) CON 13 (+1) INT 11 (+0) WIS 12 (+1) CHA 12 (+1) Saving Throws  Dex +6', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Elf)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

