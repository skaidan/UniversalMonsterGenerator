# bases1/adult-topaz-dragon.py
"""
AdultTopazDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=adult-topaz-dragon
"""
from creature_base import GlobalCreatureBaseClass


class AdultTopazDragon(GlobalCreatureBaseClass):
    """
    Huge dragon (Gem) creature - AdultTopazDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 210, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 12, 'CON': 19, 'INT': 18, 'WIS': 17, 'CHAR': 18, 'armor_class': 18, 'alignment': 'typically Chaotic Neutral Armor Class  18 (natural armor) Hit Points  210 (20d12 + 80) Speed  40 ft.', 'legendary': False, 'size': 'Huge', 'type': 'dragon (Gem)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

