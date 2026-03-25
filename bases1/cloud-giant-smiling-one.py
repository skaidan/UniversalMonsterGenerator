# bases1/cloud-giant-smiling-one.py
"""
CloudGiantSmilingOne creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cloud-giant-smiling-one
"""
from creature_base import GlobalCreatureBaseClass


class CloudGiantSmilingOne(GlobalCreatureBaseClass):
    """
    Huge Giant creature - CloudGiantSmilingOne
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 250, 'min_level': 1, 'level': 1, 'STR': 26, 'DEX': 12, 'CON': 22, 'INT': 15, 'WIS': 16, 'CHAR': 17, 'armor_class': 15, 'alignment': 'typically Chaotic Neutral Armor Class  15 (natural armor) Hit Points  250 (20d12 + 120) Speed  40 ft.', 'legendary': False, 'size': 'Huge', 'type': 'Giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

