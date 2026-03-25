# bases1/topaz-dragon-wyrmling.py
"""
TopazDragonWyrmling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=topaz-dragon-wyrmling
"""
from creature_base import GlobalCreatureBaseClass


class TopazDragonWyrmling(GlobalCreatureBaseClass):
    """
    Medium dragon (Gem) creature - TopazDragonWyrmling
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 33, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 12, 'CON': 13, 'INT': 14, 'WIS': 13, 'CHAR': 14, 'armor_class': 16, 'alignment': 'typically Chaotic Neutral Armor Class  16 (natural armor) Hit Points  33 (6d8 + 6) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'dragon (Gem)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

