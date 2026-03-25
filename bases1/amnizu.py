# bases1/amnizu.py
"""
Amnizu creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=amnizu
"""
from creature_base import GlobalCreatureBaseClass


class Amnizu(GlobalCreatureBaseClass):
    """
    Medium Fiend (Devil) creature - Amnizu
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 202, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 13, 'CON': 16, 'INT': 20, 'WIS': 12, 'CHAR': 18, 'armor_class': 21, 'alignment': 'typically Lawful Evil Armor Class  21 (natural armor) Hit Points  202 (27d8 + 81) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

