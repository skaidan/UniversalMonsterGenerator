# bases1/amethyst-dragon-wyrmling.py
"""
AmethystDragonWyrmling creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=amethyst-dragon-wyrmling
"""
from creature_base import GlobalCreatureBaseClass


class AmethystDragonWyrmling(GlobalCreatureBaseClass):
    """
    Medium dragon (Gem) creature - AmethystDragonWyrmling
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 75, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 10, 'CON': 17, 'INT': 16, 'WIS': 13, 'CHAR': 17, 'armor_class': 17, 'alignment': 'typically Neutral Armor Class  17 (natural armor) Hit Points  75 (10d8 + 30) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'dragon (Gem)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

