# bases1/githyanki-gish.py
"""
GithyankiGish creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=githyanki-gish
"""
from creature_base import GlobalCreatureBaseClass


class GithyankiGish(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Gith creature - GithyankiGish
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 130, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 15, 'CON': 14, 'INT': 16, 'WIS': 15, 'CHAR': 16, 'armor_class': 17, 'alignment': 'Wizard)', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Gith', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

