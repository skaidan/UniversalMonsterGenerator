# bases1/hutijin.py
"""
Hutijin creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hutijin
"""
from creature_base import GlobalCreatureBaseClass


class Hutijin(GlobalCreatureBaseClass):
    """
    Large Fiend (Devil) creature - Hutijin
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 200, 'min_level': 1, 'level': 1, 'STR': 27, 'DEX': 15, 'CON': 25, 'INT': 23, 'WIS': 19, 'CHAR': 25, 'armor_class': 19, 'alignment': 'Lawful Evil Armor Class  19 (natural armor) Hit Points  200 (16d10 + 112) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

