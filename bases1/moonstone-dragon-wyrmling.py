# bases1/moonstone-dragon-wyrmling.py
"""
MoonstoneDragonWyrmling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=moonstone-dragon-wyrmling
"""
from creature_base import GlobalCreatureBaseClass


class MoonstoneDragonWyrmling(GlobalCreatureBaseClass):
    """
    Medium dragon creature - MoonstoneDragonWyrmling
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 39, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 14, 'CON': 14, 'INT': 16, 'WIS': 14, 'CHAR': 17, 'armor_class': 17, 'alignment': 'typically Neutral Armor Class  17 (natural armor) Hit Points  39 (6d8 + 12) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'dragon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

