# bases1/deep-dragon-wyrmling.py
"""
DeepDragonWyrmling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=deep-dragon-wyrmling
"""
from creature_base import GlobalCreatureBaseClass


class DeepDragonWyrmling(GlobalCreatureBaseClass):
    """
    Medium Dragon creature - DeepDragonWyrmling
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 27, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 11, 'CON': 12, 'INT': 11, 'WIS': 12, 'CHAR': 13, 'armor_class': 15, 'alignment': 'typically Neutral Evil Armor Class  15 (natural armor) Hit Points  27 (5d8 + 5) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Dragon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

