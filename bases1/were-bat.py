# bases1/were-bat.py
"""
WereBat creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=were-bat
"""
from creature_base import GlobalCreatureBaseClass


class WereBat(GlobalCreatureBaseClass):
    """
    Small humanoid (Goblin creature - WereBat
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 24, 'min_level': 1, 'level': 1, 'STR': 8, 'DEX': 17, 'CON': 10, 'INT': 10, 'WIS': 12, 'CHAR': 8, 'armor_class': 13, 'alignment': 'Shapechanger)', 'legendary': False, 'size': 'Small', 'type': 'humanoid (Goblin', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

