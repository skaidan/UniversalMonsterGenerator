# bases1/air-elemental-myrmidon.py
"""
AirElementalMyrmidon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=air-elemental-myrmidon
"""
from creature_base import GlobalCreatureBaseClass


class AirElementalMyrmidon(GlobalCreatureBaseClass):
    """
    Medium Elemental creature - AirElementalMyrmidon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 117, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 14, 'CON': 14, 'INT': 9, 'WIS': 10, 'CHAR': 10, 'armor_class': 18, 'alignment': 'typically Neutral Armor Class  18 (plate) Hit Points  117 (18d8 + 36) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

