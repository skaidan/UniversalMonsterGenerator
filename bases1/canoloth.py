# bases1/canoloth.py
"""
Canoloth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=canoloth
"""
from creature_base import GlobalCreatureBaseClass


class Canoloth(GlobalCreatureBaseClass):
    """
    Medium Fiend (Yugoloth) creature - Canoloth
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 120, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 10, 'CON': 17, 'INT': 5, 'WIS': 17, 'CHAR': 12, 'armor_class': 16, 'alignment': 'typically Neutral Evil Armor Class  16 (natural armor) Hit Points  120 (16d8 + 48) Speed  50 ft. STR 18 (+4) DEX 10 (+0) CON 17 (+3) INT 5 (-3) WIS 17 (+3) CHA 12 (+1) Skills  Investigation +3', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Yugoloth)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

