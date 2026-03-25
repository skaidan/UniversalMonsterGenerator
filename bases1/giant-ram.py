# bases1/giant-ram.py
"""
GiantRam creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-ram
"""
from creature_base import GlobalCreatureBaseClass


class GiantRam(GlobalCreatureBaseClass):
    """
    Large Fey creature - GiantRam
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 28, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 12, 'CON': 18, 'INT': 3, 'WIS': 14, 'CHAR': 10, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 (natural armor) Hit Points  28 (3d10 + 12) Speed  50 ft. STR 19 (+4) DEX 12 (+1) CON 18 (+4) INT 3 (-4) WIS 14 (+2) CHA 10 (+0) Damage Resistances  cold', 'legendary': False, 'size': 'Large', 'type': 'Fey', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

