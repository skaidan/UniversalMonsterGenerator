# bases1/monodrone.py
"""
Monodrone creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=monodrone
"""
from creature_base import GlobalCreatureBaseClass


class Monodrone(GlobalCreatureBaseClass):
    """
    Medium construct creature - Monodrone
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 5, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 13, 'CON': 12, 'INT': 4, 'WIS': 10, 'CHAR': 5, 'armor_class': 15, 'alignment': 'lawful neutral Armor Class  15 (natural armor) Hit Points  5 (1d8 + 1) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

