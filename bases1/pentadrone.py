# bases1/pentadrone.py
"""
Pentadrone creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=pentadrone
"""
from creature_base import GlobalCreatureBaseClass


class Pentadrone(GlobalCreatureBaseClass):
    """
    Large construct creature - Pentadrone
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 32, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 14, 'CON': 12, 'INT': 10, 'WIS': 10, 'CHAR': 13, 'armor_class': 16, 'alignment': 'lawful neutral Armor Class  16 (natural armor) Hit Points  32 (5d10 + 5) Speed  40 ft. STR 15 (+2) DEX 14 (+2) CON 12 (+1) INT 10 (+0) WIS 10 (+0) CHA 13 (+1) Skills  Perception +4 Senses  truesight 120 ft.', 'legendary': False, 'size': 'Large', 'type': 'construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

