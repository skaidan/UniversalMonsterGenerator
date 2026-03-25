# bases1/gigant.py
"""
Gigant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gigant
"""
from creature_base import GlobalCreatureBaseClass


class Gigant(GlobalCreatureBaseClass):
    """
    Gargantuan Monstrosity creature - Gigant
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 325, 'min_level': 1, 'level': 1, 'STR': 24, 'DEX': 14, 'CON': 21, 'INT': 3, 'WIS': 14, 'CHAR': 11, 'armor_class': 17, 'alignment': 'unaligned Armor Class  17 (natural armor) Hit Points  325 (21d20 + 105) Speed  50 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

