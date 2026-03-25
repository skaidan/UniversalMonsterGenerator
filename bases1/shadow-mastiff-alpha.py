# bases1/shadow-mastiff-alpha.py
"""
ShadowMastiffAlpha creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=shadow-mastiff-alpha
"""
from creature_base import GlobalCreatureBaseClass


class ShadowMastiffAlpha(GlobalCreatureBaseClass):
    """
    Medium Monstrosity creature - ShadowMastiffAlpha
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 44, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 14, 'CON': 13, 'INT': 5, 'WIS': 12, 'CHAR': 5, 'armor_class': 12, 'alignment': 'typically Neutral Evil Armor Class  12 Hit Points  44 (8d8 + 8) Speed  40 ft. STR 16 (+3) DEX 14 (+2) CON 13 (+1) INT 5 (-3) WIS 12 (+1) CHA 5 (-3) Skills  Perception +5', 'legendary': False, 'size': 'Medium', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

