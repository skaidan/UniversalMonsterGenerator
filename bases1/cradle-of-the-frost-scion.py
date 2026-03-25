# bases1/cradle-of-the-frost-scion.py
"""
CradleOfTheFrostScion creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cradle-of-the-frost-scion
"""
from creature_base import GlobalCreatureBaseClass


class CradleOfTheFrostScion(GlobalCreatureBaseClass):
    """
    Gargantuan Elemental creature - CradleOfTheFrostScion
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 499, 'min_level': 1, 'level': 1, 'STR': 27, 'DEX': 14, 'CON': 26, 'INT': 11, 'WIS': 19, 'CHAR': 16, 'armor_class': 20, 'alignment': 'typically Neutral Evil Armor Class  20 (natural armor) Hit Points  499 (27d20 + 216) Speed  40 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

