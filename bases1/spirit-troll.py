# bases1/spirit-troll.py
"""
SpiritTroll creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=spirit-troll
"""
from creature_base import GlobalCreatureBaseClass


class SpiritTroll(GlobalCreatureBaseClass):
    """
    Large Giant creature - SpiritTroll
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 130, 'min_level': 1, 'level': 1, 'STR': 1, 'DEX': 17, 'CON': 13, 'INT': 8, 'WIS': 9, 'CHAR': 16, 'armor_class': 17, 'alignment': 'typically Chaotic Evil Armor Class  17 (natural armor) Hit Points  130 (20d10 + 20) Speed  30 ft. STR 1 (-5) DEX 17 (+3) CON 13 (+1) INT 8 (-1) WIS 9 (-1) CHA 16 (+3) Skills  Perception +3 Damage Resistances  acid', 'legendary': False, 'size': 'Large', 'type': 'Giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

