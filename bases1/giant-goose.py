# bases1/giant-goose.py
"""
GiantGoose creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-goose
"""
from creature_base import GlobalCreatureBaseClass


class GiantGoose(GlobalCreatureBaseClass):
    """
    Large Fey creature - GiantGoose
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 60, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 16, 'CON': 15, 'INT': 6, 'WIS': 14, 'CHAR': 11, 'armor_class': 13, 'alignment': 'typically Neutral Armor Class  13 Hit Points  60 (8d10 + 16) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'Fey', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

