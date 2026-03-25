# bases1/fraz-urb-luu.py
"""
FrazUrbLuu creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fraz-urb-luu
"""
from creature_base import GlobalCreatureBaseClass


class FrazUrbLuu(GlobalCreatureBaseClass):
    """
    Large Fiend (Demon) creature - FrazUrbLuu
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 337, 'min_level': 1, 'level': 1, 'STR': 29, 'DEX': 12, 'CON': 25, 'INT': 26, 'WIS': 24, 'CHAR': 26, 'armor_class': 18, 'alignment': 'Chaotic Evil Armor Class  18 (natural armor) Hit Points  337 (27d10 + 189) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

