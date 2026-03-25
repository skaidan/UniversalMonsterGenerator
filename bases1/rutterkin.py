# bases1/rutterkin.py
"""
Rutterkin creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=rutterkin
"""
from creature_base import GlobalCreatureBaseClass


class Rutterkin(GlobalCreatureBaseClass):
    """
    Medium Fiend (Demon) creature - Rutterkin
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 37, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 15, 'CON': 17, 'INT': 5, 'WIS': 12, 'CHAR': 6, 'armor_class': 12, 'alignment': 'typically Chaotic Evil Armor Class  12 Hit Points  37 (5d8 + 15) Speed  20 ft. STR 14 (+2) DEX 15 (+2) CON 17 (+3) INT 5 (-3) WIS 12 (+1) CHA 6 (-2) Damage Resistances  cold', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

