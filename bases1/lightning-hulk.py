# bases1/lightning-hulk.py
"""
LightningHulk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=lightning-hulk
"""
from creature_base import GlobalCreatureBaseClass


class LightningHulk(GlobalCreatureBaseClass):
    """
    Large Elemental creature - LightningHulk
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 102, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 21, 'CON': 16, 'INT': 14, 'WIS': 14, 'CHAR': 15, 'armor_class': 15, 'alignment': 'typically Chaotic Neutral Armor Class  15 Hit Points  102 (12d10 + 36) Speed  0 ft.', 'legendary': False, 'size': 'Large', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

