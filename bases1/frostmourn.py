# bases1/frostmourn.py
"""
Frostmourn creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=frostmourn
"""
from creature_base import GlobalCreatureBaseClass


class Frostmourn(GlobalCreatureBaseClass):
    """
    Huge Undead creature - Frostmourn
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 195, 'min_level': 1, 'level': 1, 'STR': 23, 'DEX': 9, 'CON': 21, 'INT': 9, 'WIS': 11, 'CHAR': 18, 'armor_class': 13, 'alignment': 'typically Neutral Evil Armor Class  13 (natural armor) Hit Points  195 (17d12 + 85) Speed  40 ft. STR 23 (+6) DEX 9 (-1) CON 21 (+5) INT 9 (-1) WIS 11 (+0) CHA 18 (+4) Saving Throws  Con +9', 'legendary': False, 'size': 'Huge', 'type': 'Undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

