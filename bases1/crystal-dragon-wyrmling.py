# bases1/crystal-dragon-wyrmling.py
"""
CrystalDragonWyrmling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=crystal-dragon-wyrmling
"""
from creature_base import GlobalCreatureBaseClass


class CrystalDragonWyrmling(GlobalCreatureBaseClass):
    """
    Medium dragon (Gem) creature - CrystalDragonWyrmling
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 32, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 12, 'CON': 14, 'INT': 14, 'WIS': 13, 'CHAR': 15, 'armor_class': 14, 'alignment': 'typically Chaotic Neutral Armor Class  14 (natural armor) Hit Points  32 (5d8 + 10) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'dragon (Gem)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

