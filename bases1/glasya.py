# bases1/glasya.py
"""
Glasya creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=glasya
"""
from creature_base import GlobalCreatureBaseClass


class Glasya(GlobalCreatureBaseClass):
    """
    Medium Fiend (Devil) creature - Glasya
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 380, 'min_level': 1, 'level': 1, 'STR': 22, 'DEX': 28, 'CON': 20, 'INT': 21, 'WIS': 25, 'CHAR': 28, 'armor_class': 21, 'alignment': 'Lawful Evil Armor Class  21 (natural armor) Hit Points  380 (40d8 + 200) Speed  40 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

