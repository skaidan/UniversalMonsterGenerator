# bases1/ancient-topaz-dragon.py
"""
AncientTopazDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ancient-topaz-dragon
"""
from creature_base import GlobalCreatureBaseClass


class AncientTopazDragon(GlobalCreatureBaseClass):
    """
    Gargantuan dragon (Gem) creature - AncientTopazDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 280, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 12, 'CON': 23, 'INT': 20, 'WIS': 19, 'CHAR': 20, 'armor_class': 20, 'alignment': 'typically Chaotic Neutral Armor Class  20 (natural armor) Hit Points  280 (17d20 + 102) Speed  40 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'dragon (Gem)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

