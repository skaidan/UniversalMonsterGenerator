# bases1/kender-skirmisher.py
"""
KenderSkirmisher creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=kender-skirmisher
"""
from creature_base import GlobalCreatureBaseClass


class KenderSkirmisher(GlobalCreatureBaseClass):
    """
    Small Humanoid creature - KenderSkirmisher
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 14, 'min_level': 1, 'level': 1, 'STR': 8, 'DEX': 16, 'CON': 10, 'INT': 12, 'WIS': 8, 'CHAR': 14, 'armor_class': 14, 'alignment': 'any alignment Armor Class  14 (leather armor) Hit Points  14 (4d6) Speed  30 ft. STR 8 (-1) DEX 16 (+3) CON 10 (+0) INT 12 (+1) WIS 8 (-1) CHA 14 (+2) Skills  Perception +3', 'legendary': False, 'size': 'Small', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

