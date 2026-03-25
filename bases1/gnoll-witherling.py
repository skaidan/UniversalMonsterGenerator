# bases1/gnoll-witherling.py
"""
GnollWitherling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gnoll-witherling
"""
from creature_base import GlobalCreatureBaseClass


class GnollWitherling(GlobalCreatureBaseClass):
    """
    Medium Undead creature - GnollWitherling
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 11, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 8, 'CON': 12, 'INT': 5, 'WIS': 5, 'CHAR': 5, 'armor_class': 12, 'alignment': 'typically Chaotic Evil Armor Class  12 (natural armor) Hit Points  11 (2d8 + 2) Speed  30 ft. STR 14 (+2) DEX 8 (-1) CON 12 (+1) INT 5 (-3) WIS 5 (-3) CHA 5 (-3) Damage Immunities  poison Condition Immunities  exhaustion', 'legendary': False, 'size': 'Medium', 'type': 'Undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

