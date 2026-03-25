# bases1/deep-scion.py
"""
DeepScion creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=deep-scion
"""
from creature_base import GlobalCreatureBaseClass


class DeepScion(GlobalCreatureBaseClass):
    """
    Medium Monstrosity creature - DeepScion
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 67, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 13, 'CON': 16, 'INT': 10, 'WIS': 12, 'CHAR': 14, 'armor_class': 11, 'alignment': 'typically Chaotic Evil Armor Class  11 Hit Points  67 (9d8 + 27) Speed  30 ft. (20 ft. and swim 40 ft. in hybrid form) STR 18 (+4) DEX 13 (+1) CON 16 (+3) INT 10 (+0) WIS 12 (+1) CHA 14 (+2) Saving Throws  Wis +3', 'legendary': False, 'size': 'Medium', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

