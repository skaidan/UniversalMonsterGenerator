# bases1/phoenix.py
"""
Phoenix creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=phoenix
"""
from creature_base import GlobalCreatureBaseClass


class Phoenix(GlobalCreatureBaseClass):
    """
    Gargantuan Elemental creature - Phoenix
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 175, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 26, 'CON': 25, 'INT': 2, 'WIS': 21, 'CHAR': 18, 'armor_class': 18, 'alignment': 'typically Neutral Armor Class  18 Hit Points  175 (10d20 + 70) Speed  20 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

