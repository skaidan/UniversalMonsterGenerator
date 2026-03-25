# bases1/draconian-mage.py
"""
DraconianMage creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=draconian-mage
"""
from creature_base import GlobalCreatureBaseClass


class DraconianMage(GlobalCreatureBaseClass):
    """
    Medium monstrosity creature - DraconianMage
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 40, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 10, 'CON': 11, 'INT': 11, 'WIS': 10, 'CHAR': 14, 'armor_class': 15, 'alignment': 'any alignment Armor Class  15 (natural armor) Hit Points  40 (9d8) Speed  30 ft. STR 14 (+2) DEX 10 (+0) CON 11 (+0) INT 11 (+0) WIS 10 (+0) CHA 14 (+2) Saving Throws  Int +2', 'legendary': False, 'size': 'Medium', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

