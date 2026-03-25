# bases1/muiral.py
"""
Muiral creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=muiral
"""
from creature_base import GlobalCreatureBaseClass


class Muiral(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - Muiral
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 195, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 11, 'CON': 16, 'INT': 18, 'WIS': 13, 'CHAR': 18, 'armor_class': 16, 'alignment': 'chaotic evil Armor Class  16 (natural armor) Hit Points  195 (23d10 + 69) Speed  50 ft. STR 19 (+4) DEX 11 (+0) CON 16 (+3) INT 18 (+4) WIS 13 (+1) CHA 18 (+4) Saving Throws  Con +8', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

