# bases1/hydroloth.py
"""
Hydroloth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hydroloth
"""
from creature_base import GlobalCreatureBaseClass


class Hydroloth(GlobalCreatureBaseClass):
    """
    Medium Fiend (Yugoloth) creature - Hydroloth
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 135, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 21, 'CON': 16, 'INT': 19, 'WIS': 10, 'CHAR': 14, 'armor_class': 15, 'alignment': 'typically Neutral Evil Armor Class  15 Hit Points  135 (18d8 + 54) Speed  20 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Yugoloth)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

