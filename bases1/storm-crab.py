# bases1/storm-crab.py
"""
StormCrab creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=storm-crab
"""
from creature_base import GlobalCreatureBaseClass


class StormCrab(GlobalCreatureBaseClass):
    """
    Gargantuan Monstrosity creature - StormCrab
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 155, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 10, 'CON': 21, 'INT': 5, 'WIS': 14, 'CHAR': 9, 'armor_class': 18, 'alignment': 'unaligned Armor Class  18 (natural armor) Hit Points  155 (10d20 + 50) Speed  40 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

