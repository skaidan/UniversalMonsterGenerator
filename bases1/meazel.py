# bases1/meazel.py
"""
Meazel creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=meazel
"""
from creature_base import GlobalCreatureBaseClass


class Meazel(GlobalCreatureBaseClass):
    """
    Medium Monstrosity creature - Meazel
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 35, 'min_level': 1, 'level': 1, 'STR': 8, 'DEX': 17, 'CON': 9, 'INT': 14, 'WIS': 13, 'CHAR': 10, 'armor_class': 13, 'alignment': 'typically Neutral Evil Armor Class  13 Hit Points  35 (10d8 - 10) Speed  30 ft. STR 8 (-1) DEX 17 (+3) CON 9 (-1) INT 14 (+2) WIS 13 (+1) CHA 10 (+0) Skills  Perception +3', 'legendary': False, 'size': 'Medium', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

