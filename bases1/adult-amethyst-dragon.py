# bases1/adult-amethyst-dragon.py
"""
AdultAmethystDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=adult-amethyst-dragon
"""
from creature_base import GlobalCreatureBaseClass


class AdultAmethystDragon(GlobalCreatureBaseClass):
    """
    Huge dragon (Gem) creature - AdultAmethystDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 229, 'min_level': 1, 'level': 1, 'STR': 25, 'DEX': 14, 'CON': 25, 'INT': 20, 'WIS': 17, 'CHAR': 21, 'armor_class': 19, 'alignment': 'typically Neutral Armor Class  19 (natural armor) Hit Points  229 (17d12 + 119) Speed  40 ft.', 'legendary': False, 'size': 'Huge', 'type': 'dragon (Gem)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

