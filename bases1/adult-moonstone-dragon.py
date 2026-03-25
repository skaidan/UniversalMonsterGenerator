# bases1/adult-moonstone-dragon.py
"""
AdultMoonstoneDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=adult-moonstone-dragon
"""
from creature_base import GlobalCreatureBaseClass


class AdultMoonstoneDragon(GlobalCreatureBaseClass):
    """
    Huge dragon creature - AdultMoonstoneDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 195, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 18, 'CON': 20, 'INT': 22, 'WIS': 20, 'CHAR': 23, 'armor_class': 19, 'alignment': 'typically Neutral Armor Class  19 (natural armor) Hit Points  195 (17d12 + 85) Speed  40 ft.', 'legendary': False, 'size': 'Huge', 'type': 'dragon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

