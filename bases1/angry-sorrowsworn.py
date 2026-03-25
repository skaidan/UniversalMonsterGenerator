# bases1/angry-sorrowsworn.py
"""
AngrySorrowsworn creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=angry-sorrowsworn
"""
from creature_base import GlobalCreatureBaseClass


class AngrySorrowsworn(GlobalCreatureBaseClass):
    """
    Medium Monstrosity creature - AngrySorrowsworn
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 255, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 10, 'CON': 19, 'INT': 8, 'WIS': 13, 'CHAR': 6, 'armor_class': 18, 'alignment': 'typically Neutral Evil Armor Class  18 (natural armor) Hit Points  255 (30d8 + 120) Speed  30 ft. STR 17 (+3) DEX 10 (+0) CON 19 (+4) INT 8 (-1) WIS 13 (+1) CHA 6 (-2) Skills  Perception +11 Damage Resistances  bludgeoning', 'legendary': False, 'size': 'Medium', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

