# bases1/draegloth.py
"""
Draegloth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=draegloth
"""
from creature_base import GlobalCreatureBaseClass


class Draegloth(GlobalCreatureBaseClass):
    """
    Large Fiend (Demon) creature - Draegloth
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 123, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 15, 'CON': 18, 'INT': 13, 'WIS': 11, 'CHAR': 11, 'armor_class': 15, 'alignment': 'typically Chaotic Evil Armor Class  15 (natural armor) Hit Points  123 (13d10 + 52) Speed  30 ft. STR 20 (+5) DEX 15 (+2) CON 18 (+4) INT 13 (+1) WIS 11 (+0) CHA 11 (+0) Skills  Perception +3', 'legendary': False, 'size': 'Large', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

