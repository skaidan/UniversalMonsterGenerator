# bases1/flail-snail.py
"""
FlailSnail creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=flail-snail
"""
from creature_base import GlobalCreatureBaseClass


class FlailSnail(GlobalCreatureBaseClass):
    """
    Large Elemental creature - FlailSnail
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 52, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 5, 'CON': 20, 'INT': 3, 'WIS': 10, 'CHAR': 5, 'armor_class': 16, 'alignment': 'unaligned Armor Class  16 (natural armor) Hit Points  52 (5d10 + 25) Speed  10 ft. STR 17 (+3) DEX 5 (-3) CON 20 (+5) INT 3 (-4) WIS 10 (+0) CHA 5 (-3) Damage Immunities  fire', 'legendary': False, 'size': 'Large', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

