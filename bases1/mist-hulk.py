# bases1/mist-hulk.py
"""
MistHulk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mist-hulk
"""
from creature_base import GlobalCreatureBaseClass


class MistHulk(GlobalCreatureBaseClass):
    """
    Large Elemental creature - MistHulk
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 94, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 21, 'CON': 20, 'INT': 11, 'WIS': 13, 'CHAR': 16, 'armor_class': 15, 'alignment': 'typically Chaotic Neutral Armor Class  15 Hit Points  94 (9d10 + 45) Speed  0 ft.', 'legendary': False, 'size': 'Large', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

