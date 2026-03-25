# bases1/water-elemental-myrmidon.py
"""
WaterElementalMyrmidon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=water-elemental-myrmidon
"""
from creature_base import GlobalCreatureBaseClass


class WaterElementalMyrmidon(GlobalCreatureBaseClass):
    """
    Medium Elemental creature - WaterElementalMyrmidon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 127, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 14, 'CON': 15, 'INT': 8, 'WIS': 10, 'CHAR': 10, 'armor_class': 18, 'alignment': 'typically Neutral Armor Class  18 (plate) Hit Points  127 (17d8 + 51) Speed  40 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

