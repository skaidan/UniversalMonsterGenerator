# bases1/dragon-turtle-wyrmling.py
"""
DragonTurtleWyrmling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dragon-turtle-wyrmling
"""
from creature_base import GlobalCreatureBaseClass


class DragonTurtleWyrmling(GlobalCreatureBaseClass):
    """
    Large Dragon creature - DragonTurtleWyrmling
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 90, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 10, 'CON': 15, 'INT': 8, 'WIS': 10, 'CHAR': 10, 'armor_class': 18, 'alignment': 'typically Neutral Armor Class  18 (natural armor) Hit Points  90 (12d10 + 24) Speed  20 ft.', 'legendary': False, 'size': 'Large', 'type': 'Dragon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

