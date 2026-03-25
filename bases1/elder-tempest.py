# bases1/elder-tempest.py
"""
ElderTempest creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=elder-tempest
"""
from creature_base import GlobalCreatureBaseClass


class ElderTempest(GlobalCreatureBaseClass):
    """
    Gargantuan Elemental creature - ElderTempest
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 264, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 28, 'CON': 23, 'INT': 2, 'WIS': 21, 'CHAR': 18, 'armor_class': 19, 'alignment': 'typically Neutral Armor Class  19 Hit Points  264 (16d20 + 96) Speed  0 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

