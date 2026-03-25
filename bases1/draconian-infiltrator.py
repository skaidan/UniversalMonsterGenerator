# bases1/draconian-infiltrator.py
"""
DraconianInfiltrator creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=draconian-infiltrator
"""
from creature_base import GlobalCreatureBaseClass


class DraconianInfiltrator(GlobalCreatureBaseClass):
    """
    Medium monstrosity creature - DraconianInfiltrator
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 39, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 17, 'CON': 14, 'INT': 9, 'WIS': 13, 'CHAR': 11, 'armor_class': 15, 'alignment': 'any alignment Armor Class  15 (natural armor) Hit Points  39 (6d8 + 12) Speed  40 ft.', 'legendary': False, 'size': 'Medium', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

