# bases1/geryon.py
"""
Geryon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=geryon
"""
from creature_base import GlobalCreatureBaseClass


class Geryon(GlobalCreatureBaseClass):
    """
    Huge Fiend (Devil) creature - Geryon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 300, 'min_level': 1, 'level': 1, 'STR': 29, 'DEX': 17, 'CON': 22, 'INT': 19, 'WIS': 16, 'CHAR': 23, 'armor_class': 19, 'alignment': 'Lawful Evil Armor Class  19 (natural armor) Hit Points  300 (24d12 + 144) Speed  30 ft.', 'legendary': False, 'size': 'Huge', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

