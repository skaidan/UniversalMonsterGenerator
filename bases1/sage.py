# bases1/sage.py
"""
Sage creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=sage
"""
from creature_base import GlobalCreatureBaseClass


class Sage(GlobalCreatureBaseClass):
    """
    Medium humanoid (any race) creature - Sage
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 8, 'DEX': 10, 'CON': 10, 'INT': 18, 'WIS': 15, 'CHAR': 11, 'armor_class': 10, 'alignment': '- Armor Class  10 (13 with  mage armor ) Hit Points  22 (5d8) Speed  30 ft. STR 8 (-1) DEX 10 (+0) CON 10 (+0) INT 18 (+4) WIS 15 (+2) CHA 11 (+0) Skills  Arcana +8', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (any race)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

