# bases1/thorny-vegepygmy.py
"""
ThornyVegepygmy creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=thorny-vegepygmy
"""
from creature_base import GlobalCreatureBaseClass


class ThornyVegepygmy(GlobalCreatureBaseClass):
    """
    Medium Plant creature - ThornyVegepygmy
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 27, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 12, 'CON': 13, 'INT': 2, 'WIS': 10, 'CHAR': 6, 'armor_class': 14, 'alignment': 'typically Neutral Armor Class  14 (natural armor) Hit Points  27 (5d8 + 5) Speed  30 ft. STR 13 (+1) DEX 12 (+1) CON 13 (+1) INT 2 (-4) WIS 10 (+0) CHA 6 (-2) Skills  Perception +4', 'legendary': False, 'size': 'Medium', 'type': 'Plant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

