# bases1/lonely-sorrowsworn.py
"""
LonelySorrowsworn creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=lonely-sorrowsworn
"""
from creature_base import GlobalCreatureBaseClass


class LonelySorrowsworn(GlobalCreatureBaseClass):
    """
    Medium Monstrosity creature - LonelySorrowsworn
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 112, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 12, 'CON': 17, 'INT': 6, 'WIS': 11, 'CHAR': 6, 'armor_class': 16, 'alignment': 'typically Neutral Evil Armor Class  16 (natural armor) Hit Points  112 (15d8 + 45) Speed  30 ft. STR 16 (+3) DEX 12 (+1) CON 17 (+3) INT 6 (-2) WIS 11 (+0) CHA 6 (-2) Damage Resistances  bludgeoning', 'legendary': False, 'size': 'Medium', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

