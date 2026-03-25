# bases1/stench-kow.py
"""
StenchKow creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=stench-kow
"""
from creature_base import GlobalCreatureBaseClass


class StenchKow(GlobalCreatureBaseClass):
    """
    Large Fiend (Cattle) creature - StenchKow
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 15, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 10, 'CON': 14, 'INT': 2, 'WIS': 10, 'CHAR': 4, 'armor_class': 10, 'alignment': 'unaligned Armor Class  10 Hit Points  15 (2d10 + 4) Speed  30 ft. STR 18 (+4) DEX 10 (+0) CON 14 (+2) INT 2 (-4) WIS 10 (+0) CHA 4 (-3) Damage Resistances  cold', 'legendary': False, 'size': 'Large', 'type': 'Fiend (Cattle)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

