# bases1/young-kruthik.py
"""
YoungKruthik creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=young-kruthik
"""
from creature_base import GlobalCreatureBaseClass


class YoungKruthik(GlobalCreatureBaseClass):
    """
    Small Monstrosity creature - YoungKruthik
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 9, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 16, 'CON': 13, 'INT': 4, 'WIS': 10, 'CHAR': 6, 'armor_class': 16, 'alignment': 'unaligned Armor Class  16 (natural armor) Hit Points  9 (2d6 + 2) Speed  30 ft.', 'legendary': False, 'size': 'Small', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

