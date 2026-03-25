# bases1/troll-amalgam.py
"""
TrollAmalgam creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=troll-amalgam
"""
from creature_base import GlobalCreatureBaseClass


class TrollAmalgam(GlobalCreatureBaseClass):
    """
    Gargantuan Giant creature - TrollAmalgam
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 217, 'min_level': 1, 'level': 1, 'STR': 25, 'DEX': 14, 'CON': 21, 'INT': 9, 'WIS': 16, 'CHAR': 5, 'armor_class': 15, 'alignment': 'typically Chaotic Evil Armor Class  15 (natural armor) Hit Points  217 (14d20 + 70) Speed  60 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'Giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

