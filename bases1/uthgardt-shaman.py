# bases1/uthgardt-shaman.py
"""
UthgardtShaman creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=uthgardt-shaman
"""
from creature_base import GlobalCreatureBaseClass


class UthgardtShaman(GlobalCreatureBaseClass):
    """
    Medium humanoid (Human) creature - UthgardtShaman
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 38, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 12, 'CON': 13, 'INT': 10, 'WIS': 15, 'CHAR': 12, 'armor_class': 13, 'alignment': 'neutral evil Armor Class  13 (hide armor) Hit Points  38 (7d8 + 7) Speed  30 ft. STR 14 (+2) DEX 12 (+1) CON 13 (+1) INT 10 (+0) WIS 15 (+2) CHA 12 (+1) Skills  Medicine +4', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Human)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

