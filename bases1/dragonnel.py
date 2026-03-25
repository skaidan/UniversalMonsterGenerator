# bases1/dragonnel.py
"""
Dragonnel creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dragonnel
"""
from creature_base import GlobalCreatureBaseClass


class Dragonnel(GlobalCreatureBaseClass):
    """
    Large Dragon creature - Dragonnel
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 58, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 15, 'CON': 12, 'INT': 8, 'WIS': 13, 'CHAR': 10, 'armor_class': 13, 'alignment': 'typically Neutral Armor Class  13 (natural armor) Hit Points  58 (9d10 + 9) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'Dragon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

