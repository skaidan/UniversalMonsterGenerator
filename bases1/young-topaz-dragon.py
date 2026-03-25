# bases1/young-topaz-dragon.py
"""
YoungTopazDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=young-topaz-dragon
"""
from creature_base import GlobalCreatureBaseClass


class YoungTopazDragon(GlobalCreatureBaseClass):
    """
    Large dragon (Gem) creature - YoungTopazDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 127, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 12, 'CON': 15, 'INT': 16, 'WIS': 15, 'CHAR': 16, 'armor_class': 17, 'alignment': 'typically Chaotic Neutral Armor Class  17 (natural armor) Hit Points  127 (17d10 + 34) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'dragon (Gem)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

