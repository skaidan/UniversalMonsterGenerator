# bases1/cradle-of-the-cloud-scion.py
"""
CradleOfTheCloudScion creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cradle-of-the-cloud-scion
"""
from creature_base import GlobalCreatureBaseClass


class CradleOfTheCloudScion(GlobalCreatureBaseClass):
    """
    Gargantuan Elemental creature - CradleOfTheCloudScion
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 624, 'min_level': 1, 'level': 1, 'STR': 29, 'DEX': 21, 'CON': 28, 'INT': 14, 'WIS': 22, 'CHAR': 19, 'armor_class': 19, 'alignment': 'typically Chaotic Neutral Armor Class  19 (natural armor) Hit Points  624 (32d20 + 288) Speed  0 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

