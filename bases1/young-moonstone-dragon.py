# bases1/young-moonstone-dragon.py
"""
YoungMoonstoneDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=young-moonstone-dragon
"""
from creature_base import GlobalCreatureBaseClass


class YoungMoonstoneDragon(GlobalCreatureBaseClass):
    """
    Large dragon creature - YoungMoonstoneDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 144, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 16, 'CON': 17, 'INT': 18, 'WIS': 17, 'CHAR': 19, 'armor_class': 18, 'alignment': 'typically Neutral Armor Class  18 (natural armor) Hit Points  144 (17d10 + 51) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'dragon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

