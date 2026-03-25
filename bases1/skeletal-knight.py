# bases1/skeletal-knight.py
"""
SkeletalKnight creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=skeletal-knight
"""
from creature_base import GlobalCreatureBaseClass


class SkeletalKnight(GlobalCreatureBaseClass):
    """
    Medium Undead creature - SkeletalKnight
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 112, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 10, 'CON': 16, 'INT': 13, 'WIS': 14, 'CHAR': 10, 'armor_class': 18, 'alignment': 'typically Lawful Evil Armor Class  18 (plate) Hit Points  112 (15d8 + 45) Speed  30 ft. STR 20 (+5) DEX 10 (+0) CON 16 (+3) INT 13 (+1) WIS 14 (+2) CHA 10 (+0) Saving Throws  Con +6', 'legendary': False, 'size': 'Medium', 'type': 'Undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

