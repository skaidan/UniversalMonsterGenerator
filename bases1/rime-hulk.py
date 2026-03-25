# bases1/rime-hulk.py
"""
RimeHulk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=rime-hulk
"""
from creature_base import GlobalCreatureBaseClass


class RimeHulk(GlobalCreatureBaseClass):
    """
    Large Elemental creature - RimeHulk
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 85, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 10, 'CON': 18, 'INT': 8, 'WIS': 9, 'CHAR': 6, 'armor_class': 15, 'alignment': 'typically Neutral Evil Armor Class  15 (natural armor) Hit Points  85 (9d10 + 36) Speed  30 ft. STR 18 (+4) DEX 10 (+0) CON 18 (+4) INT 8 (-1) WIS 9 (-1) CHA 6 (-2) Damage Immunities  cold', 'legendary': False, 'size': 'Large', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

