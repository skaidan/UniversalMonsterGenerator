# bases1/elder-brain.py
"""
ElderBrain creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=elder-brain
"""
from creature_base import GlobalCreatureBaseClass


class ElderBrain(GlobalCreatureBaseClass):
    """
    Large Aberration (Mind Flayer) creature - ElderBrain
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 210, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 10, 'CON': 20, 'INT': 21, 'WIS': 19, 'CHAR': 24, 'armor_class': 10, 'alignment': 'typically Lawful Evil Armor Class  10 Hit Points  210 (20d10 + 100) Speed  5 ft.', 'legendary': False, 'size': 'Large', 'type': 'Aberration (Mind Flayer)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

