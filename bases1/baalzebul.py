# bases1/baalzebul.py
"""
Baalzebul creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=baalzebul
"""
from creature_base import GlobalCreatureBaseClass


class Baalzebul(GlobalCreatureBaseClass):
    """
    Huge Fiend (Devil) creature - Baalzebul
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 540, 'min_level': 1, 'level': 1, 'STR': 28, 'DEX': 15, 'CON': 25, 'INT': 21, 'WIS': 24, 'CHAR': 26, 'armor_class': 19, 'alignment': 'Lawful Evil Armor Class  19 (natural armor) Hit Points  540 (40d12 + 280) Speed  30 ft.', 'legendary': False, 'size': 'Huge', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

