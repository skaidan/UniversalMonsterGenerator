# bases1/eyedrake.py
"""
Eyedrake creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=eyedrake
"""
from creature_base import GlobalCreatureBaseClass


class Eyedrake(GlobalCreatureBaseClass):
    """
    Large Aberration creature - Eyedrake
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 119, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 10, 'CON': 16, 'INT': 14, 'WIS': 14, 'CHAR': 16, 'armor_class': 16, 'alignment': 'typically Lawful Evil Armor Class  16 (natural armor) Hit Points  119 (14d10 + 42) Speed  O ft.', 'legendary': False, 'size': 'Large', 'type': 'Aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

