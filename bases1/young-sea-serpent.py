# bases1/young-sea-serpent.py
"""
YoungSeaSerpent creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=young-sea-serpent
"""
from creature_base import GlobalCreatureBaseClass


class YoungSeaSerpent(GlobalCreatureBaseClass):
    """
    Huge Dragon creature - YoungSeaSerpent
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 123, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 12, 'CON': 17, 'INT': 11, 'WIS': 13, 'CHAR': 10, 'armor_class': 16, 'alignment': 'typically Neutral Armor Class  16 (natural armor) Hit Points  123 (13d12 + 39) Speed  10 ft.', 'legendary': False, 'size': 'Huge', 'type': 'Dragon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

