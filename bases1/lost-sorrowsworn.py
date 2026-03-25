# bases1/lost-sorrowsworn.py
"""
LostSorrowsworn creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=lost-sorrowsworn
"""
from creature_base import GlobalCreatureBaseClass


class LostSorrowsworn(GlobalCreatureBaseClass):
    """
    Medium Monstrosity creature - LostSorrowsworn
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 78, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 12, 'CON': 15, 'INT': 6, 'WIS': 7, 'CHAR': 5, 'armor_class': 15, 'alignment': 'typically Neutral Evil Armor Class  15 (natural armor) Hit Points  78 (12d8 + 24) Speed  30 ft. STR 17 (+3) DEX 12 (+1) CON 15 (+2) INT 6 (-2) WIS 7 (-2) CHA 5 (-3) Skills  Athletics +6 Damage Resistances  bludgeoning', 'legendary': False, 'size': 'Medium', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

