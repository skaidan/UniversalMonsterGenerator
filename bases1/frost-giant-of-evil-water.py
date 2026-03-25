# bases1/frost-giant-of-evil-water.py
"""
FrostGiantOfEvilWater creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=frost-giant-of-evil-water
"""
from creature_base import GlobalCreatureBaseClass


class FrostGiantOfEvilWater(GlobalCreatureBaseClass):
    """
    Huge Giant creature - FrostGiantOfEvilWater
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 172, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 16, 'CON': 21, 'INT': 9, 'WIS': 14, 'CHAR': 12, 'armor_class': 16, 'alignment': 'typically Neutral Evil Armor Class  16 (scale mail) Hit Points  172 (15d12 + 75) Speed  40 ft.', 'legendary': False, 'size': 'Huge', 'type': 'Giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

