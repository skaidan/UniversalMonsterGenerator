# bases1/death-kiss.py
"""
DeathKiss creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=death-kiss
"""
from creature_base import GlobalCreatureBaseClass


class DeathKiss(GlobalCreatureBaseClass):
    """
    Large Aberration (Beholder) creature - DeathKiss
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 142, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 14, 'CON': 18, 'INT': 10, 'WIS': 12, 'CHAR': 10, 'armor_class': 15, 'alignment': 'typically Neutral Evil Armor Class  15 (natural armor) Hit Points  142 (15d10 + 60) Speed  0 ft.', 'legendary': False, 'size': 'Large', 'type': 'Aberration (Beholder)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

