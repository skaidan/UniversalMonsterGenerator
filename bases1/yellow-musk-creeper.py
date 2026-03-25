# bases1/yellow-musk-creeper.py
"""
YellowMuskCreeper creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yellow-musk-creeper
"""
from creature_base import GlobalCreatureBaseClass


class YellowMuskCreeper(GlobalCreatureBaseClass):
    """
    Medium plant creature - YellowMuskCreeper
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 60, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 3, 'CON': 12, 'INT': 1, 'WIS': 10, 'CHAR': 3, 'armor_class': 6, 'alignment': 'unaligned Armor Class  6 Hit Points  60 (11d8 + 11) Speed  5 ft.', 'legendary': False, 'size': 'Medium', 'type': 'plant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

