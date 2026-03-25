# bases1/marut.py
"""
Marut creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=marut
"""
from creature_base import GlobalCreatureBaseClass


class Marut(GlobalCreatureBaseClass):
    """
    Large Construct (Inevitable) creature - Marut
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 432, 'min_level': 1, 'level': 1, 'STR': 28, 'DEX': 12, 'CON': 26, 'INT': 19, 'WIS': 15, 'CHAR': 18, 'armor_class': 22, 'alignment': 'typically Lawful Neutral Armor Class  22 (natural armor) Hit Points  432 (32d10 + 256) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'Construct (Inevitable)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

