# bases1/storm-giant-tempest-caller.py
"""
StormGiantTempestCaller creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=storm-giant-tempest-caller
"""
from creature_base import GlobalCreatureBaseClass


class StormGiantTempestCaller(GlobalCreatureBaseClass):
    """
    Huge Giant (Sorcerer) creature - StormGiantTempestCaller
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 310, 'min_level': 1, 'level': 1, 'STR': 29, 'DEX': 14, 'CON': 20, 'INT': 21, 'WIS': 18, 'CHAR': 25, 'armor_class': 17, 'alignment': 'any alignment Armor Class  17 (natural armor) Hit Points  310 (27d12 + 135) Speed  50 ft.', 'legendary': False, 'size': 'Huge', 'type': 'Giant (Sorcerer)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

