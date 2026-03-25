# bases1/korred.py
"""
Korred creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=korred
"""
from creature_base import GlobalCreatureBaseClass


class Korred(GlobalCreatureBaseClass):
    """
    Small Fey creature - Korred
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 93, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 14, 'CON': 20, 'INT': 10, 'WIS': 15, 'CHAR': 9, 'armor_class': 17, 'alignment': 'typically Chaotic Neutral Armor Class  17 (natural armor) Hit Points  93 (11d6 + 55) Speed  30 ft.', 'legendary': False, 'size': 'Small', 'type': 'Fey', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

