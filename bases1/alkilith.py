# bases1/alkilith.py
"""
Alkilith creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=alkilith
"""
from creature_base import GlobalCreatureBaseClass


class Alkilith(GlobalCreatureBaseClass):
    """
    Medium Fiend (Demon) creature - Alkilith
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 168, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 19, 'CON': 22, 'INT': 6, 'WIS': 11, 'CHAR': 7, 'armor_class': 17, 'alignment': 'typically Chaotic Evil Armor Class  17 (natural armor) Hit Points  168 (16d8 + 96) Speed  40 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

