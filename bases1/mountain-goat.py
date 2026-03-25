# bases1/mountain-goat.py
"""
MountainGoat creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mountain-goat
"""
from creature_base import GlobalCreatureBaseClass


class MountainGoat(GlobalCreatureBaseClass):
    """
    Medium beast creature - MountainGoat
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 13, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 12, 'CON': 14, 'INT': 2, 'WIS': 10, 'CHAR': 5, 'armor_class': 11, 'alignment': 'unaligned Armor Class  11 Hit Points  13 (2d8 + 4) Speed  40 ft.', 'legendary': False, 'size': 'Medium', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

