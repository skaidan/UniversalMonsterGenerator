# bases1/ogremoch.py
"""
Ogremoch creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ogremoch
"""
from creature_base import GlobalCreatureBaseClass


class Ogremoch(GlobalCreatureBaseClass):
    """
    Gargantuan elemental creature - Ogremoch
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 526, 'min_level': 1, 'level': 1, 'STR': 26, 'DEX': 11, 'CON': 28, 'INT': 11, 'WIS': 15, 'CHAR': 22, 'armor_class': 20, 'alignment': 'neutral evil Armor Class  20 (natural armor) Hit Points  526 (27d20 + 243) Speed  50 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

