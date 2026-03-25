# bases1/death-s-head-of-bhaal.py
"""
DeathSHeadOfBhaal creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=death-s-head-of-bhaal
"""
from creature_base import GlobalCreatureBaseClass


class DeathSHeadOfBhaal(GlobalCreatureBaseClass):
    """
    Medium humanoid (Human) creature - DeathSHeadOfBhaal
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 76, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 20, 'CON': 20, 'INT': 14, 'WIS': 13, 'CHAR': 16, 'armor_class': 15, 'alignment': 'chaotic evil Armor Class  15 Hit Points  76 (8d8 + 40) Speed  50 ft. STR 20 (+5) DEX 20 (+5) CON 20 (+5) INT 14 (+2) WIS 13 (+1) CHA 16 (+3) Skills  Intimidation +6', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Human)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

