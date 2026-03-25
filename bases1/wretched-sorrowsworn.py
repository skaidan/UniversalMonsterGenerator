# bases1/wretched-sorrowsworn.py
"""
WretchedSorrowsworn creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=wretched-sorrowsworn
"""
from creature_base import GlobalCreatureBaseClass


class WretchedSorrowsworn(GlobalCreatureBaseClass):
    """
    Small Monstrosity creature - WretchedSorrowsworn
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 10, 'min_level': 1, 'level': 1, 'STR': 7, 'DEX': 12, 'CON': 9, 'INT': 5, 'WIS': 6, 'CHAR': 5, 'armor_class': 15, 'alignment': 'typically Neutral Evil Armor Class  15 (natural armor) Hit Points  10 (4d6 - 4) Speed  40 ft. STR 7 (-2) DEX 12 (+1) CON 9 (-1) INT 5 (-3) WIS 6 (-2) CHA 5 (-3) Damage Resistances  bludgeoning', 'legendary': False, 'size': 'Small', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

