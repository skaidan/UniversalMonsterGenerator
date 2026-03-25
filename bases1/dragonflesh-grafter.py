# bases1/dragonflesh-grafter.py
"""
DragonfleshGrafter creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dragonflesh-grafter
"""
from creature_base import GlobalCreatureBaseClass


class DragonfleshGrafter(GlobalCreatureBaseClass):
    """
    Large Monstrosity creature - DragonfleshGrafter
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 52, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 11, 'CON': 14, 'INT': 10, 'WIS': 10, 'CHAR': 6, 'armor_class': 14, 'alignment': 'typically Neutral Evil Armor Class  14 (natural armor) Hit Points  52 (7d10 + 14) Speed  30 ft. STR 16 (+3) DEX 11 (+0) CON 14 (+2) INT 10 (+0) WIS 10 (+0) CHA 6 (-2) Saving Throws  Str +5', 'legendary': False, 'size': 'Large', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

