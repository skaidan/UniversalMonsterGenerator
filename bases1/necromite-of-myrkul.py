# bases1/necromite-of-myrkul.py
"""
NecromiteOfMyrkul creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=necromite-of-myrkul
"""
from creature_base import GlobalCreatureBaseClass


class NecromiteOfMyrkul(GlobalCreatureBaseClass):
    """
    Medium humanoid (Human) creature - NecromiteOfMyrkul
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 13, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 13, 'CON': 15, 'INT': 16, 'WIS': 11, 'CHAR': 10, 'armor_class': 11, 'alignment': 'neutral evil Armor Class  11 Hit Points  13 (2d8 + 4) Speed  30 ft. STR 10 (+0) DEX 13 (+1) CON 15 (+2) INT 16 (+3) WIS 11 (+0) CHA 10 (+0) Skills  Arcana +5', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Human)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

