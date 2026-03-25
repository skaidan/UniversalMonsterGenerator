# bases1/hoard-mimic.py
"""
HoardMimic creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hoard-mimic
"""
from creature_base import GlobalCreatureBaseClass


class HoardMimic(GlobalCreatureBaseClass):
    """
    Huge Monstrosity creature - HoardMimic
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 123, 'min_level': 1, 'level': 1, 'STR': 21, 'DEX': 12, 'CON': 17, 'INT': 10, 'WIS': 16, 'CHAR': 10, 'armor_class': 14, 'alignment': 'typically Neutral Armor Class  14 (natural armor) Hit Points  123 (13d12 + 39) Speed  30 ft. STR 21 (+5) DEX 12 (+1) CON 17 (+3) INT 10 (+0) WIS 16 (+3) CHA 10 (+0) Saving Throws  Con +6', 'legendary': False, 'size': 'Huge', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

