# bases1/howler.py
"""
Howler creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=howler
"""
from creature_base import GlobalCreatureBaseClass


class Howler(GlobalCreatureBaseClass):
    """
    Large Fiend creature - Howler
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 90, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 16, 'CON': 15, 'INT': 5, 'WIS': 20, 'CHAR': 6, 'armor_class': 16, 'alignment': 'typically Chaotic Evil Armor Class  16 (natural armor) Hit Points  90 (12d10 + 24) Speed  40 ft. STR 17 (+3) DEX 16 (+3) CON 15 (+2) INT 5 (-3) WIS 20 (+5) CHA 6 (-2) Skills  Perception +5 Damage Resistances  cold', 'legendary': False, 'size': 'Large', 'type': 'Fiend', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

