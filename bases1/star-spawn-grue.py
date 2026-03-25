# bases1/star-spawn-grue.py
"""
StarSpawnGrue creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=star-spawn-grue
"""
from creature_base import GlobalCreatureBaseClass


class StarSpawnGrue(GlobalCreatureBaseClass):
    """
    Small Aberration creature - StarSpawnGrue
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 17, 'min_level': 1, 'level': 1, 'STR': 6, 'DEX': 13, 'CON': 10, 'INT': 9, 'WIS': 11, 'CHAR': 6, 'armor_class': 11, 'alignment': 'typically Neutral Evil Armor Class  11 Hit Points  17 (5d6) Speed  30 ft. STR 6 (-2) DEX 13 (+1) CON 10 (+0) INT 9 (-1) WIS 11 (+0) CHA 6 (-2) Damage Immunities  psychic Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Small', 'type': 'Aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

