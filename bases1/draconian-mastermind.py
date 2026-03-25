# bases1/draconian-mastermind.py
"""
DraconianMastermind creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=draconian-mastermind
"""
from creature_base import GlobalCreatureBaseClass


class DraconianMastermind(GlobalCreatureBaseClass):
    """
    Medium monstrosity creature - DraconianMastermind
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 67, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 14, 'CON': 16, 'INT': 15, 'WIS': 11, 'CHAR': 17, 'armor_class': 17, 'alignment': 'any alignment Armor Class  17 (natural armor) Hit Points  67 (9d8 + 27) Speed  30 ft. STR 13 (+1) DEX 14 (+2) CON 16 (+3) INT 15 (+2) WIS 11 (+0) CHA 17 (+3) Saving Throws  Int +5', 'legendary': False, 'size': 'Medium', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

