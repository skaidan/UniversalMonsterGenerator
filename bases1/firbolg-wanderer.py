# bases1/firbolg-wanderer.py
"""
FirbolgWanderer creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=firbolg-wanderer
"""
from creature_base import GlobalCreatureBaseClass


class FirbolgWanderer(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Cleric) creature - FirbolgWanderer
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 90, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 14, 'CON': 16, 'INT': 14, 'WIS': 17, 'CHAR': 16, 'armor_class': 16, 'alignment': 'any alignment Armor Class  16 (breastplate) Hit Points  90 (12d8 + 36) Speed  30 ft. STR 16 (+3) DEX 14 (+2) CON 16 (+3) INT 14 (+2) WIS 17 (+3) CHA 16 (+3) Saving Throws  Dex +5', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Cleric)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

