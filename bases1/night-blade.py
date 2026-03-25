# bases1/night-blade.py
"""
NightBlade creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=night-blade
"""
from creature_base import GlobalCreatureBaseClass


class NightBlade(GlobalCreatureBaseClass):
    """
    Medium humanoid (Human) creature - NightBlade
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 11, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 15, 'CON': 12, 'INT': 10, 'WIS': 11, 'CHAR': 14, 'armor_class': 12, 'alignment': 'chaotic evil Armor Class  12 Hit Points  11 (2d8 + 2) Speed  40 ft. STR 11 (+0) DEX 15 (+2) CON 12 (+1) INT 10 (+0) WIS 11 (+0) CHA 14 (+2) Skills  Intimidation +4', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Human)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

