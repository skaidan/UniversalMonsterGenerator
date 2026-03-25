# bases1/dragonflesh-abomination.py
"""
DragonfleshAbomination creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dragonflesh-abomination
"""
from creature_base import GlobalCreatureBaseClass


class DragonfleshAbomination(GlobalCreatureBaseClass):
    """
    Huge Monstrosity creature - DragonfleshAbomination
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 66, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 14, 'CON': 17, 'INT': 5, 'WIS': 12, 'CHAR': 6, 'armor_class': 15, 'alignment': 'typically Neutral Evil Armor Class  15 (natural armor) Hit Points  66 (7d12 + 21) Speed  30 ft. fly 40 ft. STR 18 (+4) DEX 14 (+2) CON 17 (+3) INT 5 (-3) WIS 12 (+1) CHA 6 (-2) Saving Throws  Str +7', 'legendary': False, 'size': 'Huge', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

