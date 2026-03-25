# bases1/dolphin-delighter.py
"""
DolphinDelighter creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dolphin-delighter
"""
from creature_base import GlobalCreatureBaseClass


class DolphinDelighter(GlobalCreatureBaseClass):
    """
    Medium Fey creature - DolphinDelighter
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 27, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 13, 'CON': 13, 'INT': 11, 'WIS': 12, 'CHAR': 16, 'armor_class': 14, 'alignment': 'typically Chaotic Good Armor Class  14 (natural armor) Hit Points  27 (5d8 + 5) Speed  0 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Fey', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

