# bases1/steel-predator.py
"""
SteelPredator creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=steel-predator
"""
from creature_base import GlobalCreatureBaseClass


class SteelPredator(GlobalCreatureBaseClass):
    """
    Large Construct creature - SteelPredator
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 207, 'min_level': 1, 'level': 1, 'STR': 24, 'DEX': 17, 'CON': 22, 'INT': 4, 'WIS': 14, 'CHAR': 6, 'armor_class': 20, 'alignment': 'typically Lawful Neutral Armor Class  20 (natural armor) Hit Points  207 (18d10 + 108) Speed  40 ft. STR 24 (+7) DEX 17 (+3) CON 22 (+6) INT 4 (-3) WIS 14 (+2) CHA 6 (-2) Skills  Perception +7', 'legendary': False, 'size': 'Large', 'type': 'Construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

