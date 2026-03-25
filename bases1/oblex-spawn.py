# bases1/oblex-spawn.py
"""
OblexSpawn creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=oblex-spawn
"""
from creature_base import GlobalCreatureBaseClass


class OblexSpawn(GlobalCreatureBaseClass):
    """
    Tiny Ooze creature - OblexSpawn
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 18, 'min_level': 1, 'level': 1, 'STR': 8, 'DEX': 16, 'CON': 15, 'INT': 14, 'WIS': 11, 'CHAR': 10, 'armor_class': 13, 'alignment': 'typically Lawful Evil Armor Class  13 Hit Points  18 (4d4 + 8) Speed  20 ft. STR 8 (-1) DEX 16 (+3) CON 15 (+2) INT 14 (+2) WIS 11 (+0) CHA 10 (+0) Saving Throws  Int +4', 'legendary': False, 'size': 'Tiny', 'type': 'Ooze', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

