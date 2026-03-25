# bases1/zaratan.py
"""
Zaratan creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=zaratan
"""
from creature_base import GlobalCreatureBaseClass


class Zaratan(GlobalCreatureBaseClass):
    """
    Gargantuan Elemental creature - Zaratan
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 307, 'min_level': 1, 'level': 1, 'STR': 30, 'DEX': 10, 'CON': 30, 'INT': 2, 'WIS': 21, 'CHAR': 18, 'armor_class': 21, 'alignment': 'typically Neutral Armor Class  21 (natural armor) Hit Points  307 (15d20 + 150) Speed  40 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

