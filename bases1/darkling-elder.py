# bases1/darkling-elder.py
"""
DarklingElder creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=darkling-elder
"""
from creature_base import GlobalCreatureBaseClass


class DarklingElder(GlobalCreatureBaseClass):
    """
    Medium Fey creature - DarklingElder
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 27, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 17, 'CON': 12, 'INT': 10, 'WIS': 14, 'CHAR': 13, 'armor_class': 15, 'alignment': 'typically Chaotic Neutral Armor Class  15 (studded leather armor) Hit Points  27 (5d8 + 5) Speed  30 ft. STR 13 (+1) DEX 17 (+3) CON 12 (+1) INT 10 (+0) WIS 14 (+2) CHA 13 (+1) Skills  Acrobatics +5', 'legendary': False, 'size': 'Medium', 'type': 'Fey', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

