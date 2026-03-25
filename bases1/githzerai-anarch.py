# bases1/githzerai-anarch.py
"""
GithzeraiAnarch creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=githzerai-anarch
"""
from creature_base import GlobalCreatureBaseClass


class GithzeraiAnarch(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Gith) creature - GithzeraiAnarch
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 144, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 21, 'CON': 18, 'INT': 18, 'WIS': 20, 'CHAR': 14, 'armor_class': 20, 'alignment': 'any alignment Armor Class  20 (psychic defense) Hit Points  144 (17d8 + 68) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Gith)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

