# bases1/master-of-souls.py
"""
MasterOfSouls creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=master-of-souls
"""
from creature_base import GlobalCreatureBaseClass


class MasterOfSouls(GlobalCreatureBaseClass):
    """
    Medium humanoid (Human) creature - MasterOfSouls
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 45, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 14, 'CON': 17, 'INT': 19, 'WIS': 14, 'CHAR': 13, 'armor_class': 12, 'alignment': 'neutral evil Armor Class  12 Hit Points  45 (6d8 + 18) Speed  30 ft. STR 10 (+0) DEX 14 (+2) CON 17 (+3) INT 19 (+4) WIS 14 (+2) CHA 13 (+1) Saving Throws  Wis +4 Skills  Arcana +6', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Human)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

