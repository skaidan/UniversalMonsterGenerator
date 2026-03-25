# bases1/elder-brain-dragon.py
"""
ElderBrainDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=elder-brain-dragon
"""
from creature_base import GlobalCreatureBaseClass


class ElderBrainDragon(GlobalCreatureBaseClass):
    """
    Gargantuan Aberration creature - ElderBrainDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 350, 'min_level': 1, 'level': 1, 'STR': 27, 'DEX': 13, 'CON': 25, 'INT': 21, 'WIS': 19, 'CHAR': 24, 'armor_class': 17, 'alignment': 'typically Lawful Evil Armor Class  17 (natural armor) Hit Points  350 (20d20 + 140) Speed  40 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'Aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

