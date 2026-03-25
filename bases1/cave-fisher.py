# bases1/cave-fisher.py
"""
CaveFisher creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cave-fisher
"""
from creature_base import GlobalCreatureBaseClass


class CaveFisher(GlobalCreatureBaseClass):
    """
    Medium Monstrosity creature - CaveFisher
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 58, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 13, 'CON': 14, 'INT': 3, 'WIS': 10, 'CHAR': 3, 'armor_class': 16, 'alignment': 'unaligned Armor Class  16 (natural armor) Hit Points  58 (9d8 + 18) Speed  20 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

