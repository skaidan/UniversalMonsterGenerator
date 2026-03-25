# bases1/cradle-of-the-storm-scion.py
"""
CradleOfTheStormScion creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cradle-of-the-storm-scion
"""
from creature_base import GlobalCreatureBaseClass


class CradleOfTheStormScion(GlobalCreatureBaseClass):
    """
    Gargantuan Elemental creature - CradleOfTheStormScion
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 682, 'min_level': 1, 'level': 1, 'STR': 30, 'DEX': 14, 'CON': 29, 'INT': 16, 'WIS': 23, 'CHAR': 18, 'armor_class': 19, 'alignment': 'typically Chaotic Good Armor Class  19 (natural armor) Hit Points  682 (35d20 + 315) Speed  40 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

