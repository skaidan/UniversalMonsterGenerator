# bases1/tlincalli.py
"""
Tlincalli creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=tlincalli
"""
from creature_base import GlobalCreatureBaseClass


class Tlincalli(GlobalCreatureBaseClass):
    """
    Large Monstrosity creature - Tlincalli
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 85, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 13, 'CON': 16, 'INT': 8, 'WIS': 12, 'CHAR': 8, 'armor_class': 15, 'alignment': 'typically Neutral Armor Class  15 (natural armor) Hit Points  85 (10d10 + 30) Speed  40 ft. STR 16 (+3) DEX 13 (+1) CON 16 (+3) INT 8 (-1) WIS 12 (+1) CHA 8 (-1) Skills  Perception +4', 'legendary': False, 'size': 'Large', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

