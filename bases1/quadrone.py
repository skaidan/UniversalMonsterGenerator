# bases1/quadrone.py
"""
Quadrone creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=quadrone
"""
from creature_base import GlobalCreatureBaseClass


class Quadrone(GlobalCreatureBaseClass):
    """
    Medium construct creature - Quadrone
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 14, 'CON': 12, 'INT': 10, 'WIS': 10, 'CHAR': 11, 'armor_class': 16, 'alignment': 'lawful neutral Armor Class  16 (natural armor) Hit Points  22 (4d8 + 4) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

