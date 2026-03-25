# bases1/adult-deep-dragon.py
"""
AdultDeepDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=adult-deep-dragon
"""
from creature_base import GlobalCreatureBaseClass


class AdultDeepDragon(GlobalCreatureBaseClass):
    """
    Huge dragon creature - AdultDeepDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 147, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 14, 'CON': 18, 'INT': 16, 'WIS': 16, 'CHAR': 18, 'armor_class': 17, 'alignment': 'typically Neutral Evil Armor Class  17 (natural armor) Hit Points  147 (14d12 + 56) Speed  40 ft.', 'legendary': False, 'size': 'Huge', 'type': 'dragon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

