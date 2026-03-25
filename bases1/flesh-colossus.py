# bases1/flesh-colossus.py
"""
FleshColossus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=flesh-colossus
"""
from creature_base import GlobalCreatureBaseClass


class FleshColossus(GlobalCreatureBaseClass):
    """
    Gargantuan Construct creature - FleshColossus
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 280, 'min_level': 1, 'level': 1, 'STR': 24, 'DEX': 9, 'CON': 24, 'INT': 6, 'WIS': 10, 'CHAR': 5, 'armor_class': 14, 'alignment': 'unaligned Armor Class  14 (natural armor) Hit Points  280 (16d20 + 112) Speed  60 ft. STR 24 (+7) DEX 9 (-1) CON 24 (+7) INT 6 (-2) WIS 10 (+0) CHA 5 (-3) Damage Immunities  lightning', 'legendary': False, 'size': 'Gargantuan', 'type': 'Construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

