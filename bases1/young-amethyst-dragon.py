# bases1/young-amethyst-dragon.py
"""
YoungAmethystDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=young-amethyst-dragon
"""
from creature_base import GlobalCreatureBaseClass


class YoungAmethystDragon(GlobalCreatureBaseClass):
    """
    Large dragon (Gem) creature - YoungAmethystDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 168, 'min_level': 1, 'level': 1, 'STR': 21, 'DEX': 12, 'CON': 21, 'INT': 18, 'WIS': 15, 'CHAR': 19, 'armor_class': 18, 'alignment': 'typically Neutral Armor Class  18 (natural armor) Hit Points  168 (16d10 + 80) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'dragon (Gem)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

