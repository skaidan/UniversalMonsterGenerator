# bases1/troll-mutate.py
"""
TrollMutate creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=troll-mutate
"""
from creature_base import GlobalCreatureBaseClass


class TrollMutate(GlobalCreatureBaseClass):
    """
    Large Giant creature - TrollMutate
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 95, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 13, 'CON': 18, 'INT': 17, 'WIS': 9, 'CHAR': 12, 'armor_class': 16, 'alignment': 'typically Chaotic Evil Armor Class  16 (natural armor) Hit Points  95 (10d10 + 40) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'Giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

