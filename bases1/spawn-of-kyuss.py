# bases1/spawn-of-kyuss.py
"""
SpawnOfKyuss creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=spawn-of-kyuss
"""
from creature_base import GlobalCreatureBaseClass


class SpawnOfKyuss(GlobalCreatureBaseClass):
    """
    Medium Undead creature - SpawnOfKyuss
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 76, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 11, 'CON': 18, 'INT': 5, 'WIS': 7, 'CHAR': 3, 'armor_class': 10, 'alignment': 'typically Chaotic Evil Armor Class  10 Hit Points  76 (9d8 + 36) Speed  30 ft. STR 16 (+3) DEX 11 (+0) CON 18 (+4) INT 5 (-3) WIS 7 (-2) CHA 3 (-4) Saving Throws  Wis +1 Damage Immunities  poison Condition Immunities  exhaustion', 'legendary': False, 'size': 'Medium', 'type': 'Undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

