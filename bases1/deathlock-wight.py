# bases1/deathlock-wight.py
"""
DeathlockWight creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=deathlock-wight
"""
from creature_base import GlobalCreatureBaseClass


class DeathlockWight(GlobalCreatureBaseClass):
    """
    Medium Undead (Warlock) creature - DeathlockWight
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 37, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 14, 'CON': 16, 'INT': 12, 'WIS': 14, 'CHAR': 16, 'armor_class': 12, 'alignment': 'typically Neutral Evil Armor Class  12 (15 with  mage armor ) Hit Points  37 (5d8 + 15) Speed  30 ft. STR 11 (+0) DEX 14 (+2) CON 16 (+3) INT 12 (+1) WIS 14 (+2) CHA 16 (+3) Saving Throws  Wis +4 Skills  Arcana +3', 'legendary': False, 'size': 'Medium', 'type': 'Undead (Warlock)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

