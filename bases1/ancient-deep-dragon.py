# bases1/ancient-deep-dragon.py
"""
AncientDeepDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ancient-deep-dragon
"""
from creature_base import GlobalCreatureBaseClass


class AncientDeepDragon(GlobalCreatureBaseClass):
    """
    Gargantuan Dragon creature - AncientDeepDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 201, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 16, 'CON': 20, 'INT': 19, 'WIS': 18, 'CHAR': 21, 'armor_class': 20, 'alignment': 'typically Neutral Evil Armor Class  20 (natural armor) Hit Points  201 (13d20 + 65) Speed  40 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'Dragon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

