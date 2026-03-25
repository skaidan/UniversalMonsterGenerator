# bases1/knucklehead-trout.py
"""
KnuckleheadTrout creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=knucklehead-trout
"""
from creature_base import GlobalCreatureBaseClass


class KnuckleheadTrout(GlobalCreatureBaseClass):
    """
    Small beast creature - KnuckleheadTrout
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 7, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 14, 'CON': 11, 'INT': 1, 'WIS': 6, 'CHAR': 1, 'armor_class': 12, 'alignment': 'unaligned Armor Class  12 Hit Points  7 (2d6) Speed  0 ft.', 'legendary': False, 'size': 'Small', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

