# bases1/fomorian-noble.py
"""
FomorianNoble creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fomorian-noble
"""
from creature_base import GlobalCreatureBaseClass


class FomorianNoble(GlobalCreatureBaseClass):
    """
    Huge Giant (Wizard) creature - FomorianNoble
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 253, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 18, 'CON': 20, 'INT': 19, 'WIS': 14, 'CHAR': 16, 'armor_class': 14, 'alignment': 'typically Chaotic Evil Armor Class  14 (17 with  mage armor ) Hit Points  253 (22d12 + 110) Speed  30 ft. STR 23 (+6) DEX 18 (+4) CON 20 (+5) INT 19 (+4) WIS 14 (+2) CHA 16 (+3) Saving Throws  Int +9', 'legendary': False, 'size': 'Huge', 'type': 'Giant (Wizard)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

