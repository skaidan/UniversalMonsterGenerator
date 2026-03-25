# bases1/dragonborn-of-tiamat.py
"""
DragonbornOfTiamat creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dragonborn-of-tiamat
"""
from creature_base import GlobalCreatureBaseClass


class DragonbornOfTiamat(GlobalCreatureBaseClass):
    """
    Medium humanoid creature - DragonbornOfTiamat
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 85, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 11, 'CON': 18, 'INT': 10, 'WIS': 12, 'CHAR': 16, 'armor_class': 18, 'alignment': 'typically Chaotic Evil Armor Class  18 (plate) Hit Points  85 (10d8 + 40) Speed  30 ft. STR 20 (+5) DEX 11 (+0) CON 18 (+4) INT 10 (+0) WIS 12 (+1) CHA 16 (+3) Saving Throws  Str +8', 'legendary': False, 'size': 'Medium', 'type': 'humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

