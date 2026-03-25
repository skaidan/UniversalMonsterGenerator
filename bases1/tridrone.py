# bases1/tridrone.py
"""
Tridrone creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=tridrone
"""
from creature_base import GlobalCreatureBaseClass


class Tridrone(GlobalCreatureBaseClass):
    """
    Medium construct creature - Tridrone
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 16, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 13, 'CON': 12, 'INT': 9, 'WIS': 10, 'CHAR': 9, 'armor_class': 15, 'alignment': 'lawful neutral Armor Class  15 (natural armor) Hit Points  16 (3d8 + 3) Speed  30 ft. STR 12 (+1) DEX 13 (+1) CON 12 (+1) INT 9 (-1) WIS 10 (+0) CHA 9 (-1) Senses  truesight 120 ft.', 'legendary': False, 'size': 'Medium', 'type': 'construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

