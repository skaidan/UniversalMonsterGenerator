# bases1/duodrone.py
"""
Duodrone creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=duodrone
"""
from creature_base import GlobalCreatureBaseClass


class Duodrone(GlobalCreatureBaseClass):
    """
    Medium construct creature - Duodrone
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 11, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 13, 'CON': 12, 'INT': 6, 'WIS': 10, 'CHAR': 7, 'armor_class': 15, 'alignment': 'lawful neutral Armor Class  15 (natural armor) Hit Points  11 (2d8 + 2) Speed  30 ft. STR 11 (+0) DEX 13 (+1) CON 12 (+1) INT 6 (-2) WIS 10 (+0) CHA 7 (-2) Senses  truesight 120 ft.', 'legendary': False, 'size': 'Medium', 'type': 'construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

