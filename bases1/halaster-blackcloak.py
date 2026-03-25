# bases1/halaster-blackcloak.py
"""
HalasterBlackcloak creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=halaster-blackcloak
"""
from creature_base import GlobalCreatureBaseClass


class HalasterBlackcloak(GlobalCreatureBaseClass):
    """
    Medium humanoid (Human) creature - HalasterBlackcloak
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 246, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 18, 'CON': 18, 'INT': 24, 'WIS': 18, 'CHAR': 18, 'armor_class': 14, 'alignment': 'chaotic evil Armor Class  14 (17 with  mage armor ) Hit Points  246 (29d8 + 116) Speed  30 ft. STR 10 (+0) DEX 18 (+4) CON 18 (+4) INT 24 (+7) WIS 18 (+4) CHA 18 (+4) Saving Throws  Int +14', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Human)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

