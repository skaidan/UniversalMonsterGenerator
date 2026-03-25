# bases1/fensir-devourer.py
"""
FensirDevourer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fensir-devourer
"""
from creature_base import GlobalCreatureBaseClass


class FensirDevourer(GlobalCreatureBaseClass):
    """
    Huge Celestial creature - FensirDevourer
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 138, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 10, 'CON': 21, 'INT': 10, 'WIS': 14, 'CHAR': 11, 'armor_class': 17, 'alignment': 'typically Chaotic Neutral Armor Class  17 (natural armor) Hit Points  138 (12d12 + 60) Speed  40 ft. STR 20 (+5) DEX 10 (+0) CON 21 (+5) INT 10 (+0) WIS 14 (+2) CHA 11 (+0) Skills  Perception +8', 'legendary': False, 'size': 'Huge', 'type': 'Celestial', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

