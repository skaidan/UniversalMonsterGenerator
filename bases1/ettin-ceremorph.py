# bases1/ettin-ceremorph.py
"""
EttinCeremorph creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ettin-ceremorph
"""
from creature_base import GlobalCreatureBaseClass


class EttinCeremorph(GlobalCreatureBaseClass):
    """
    Large Aberration creature - EttinCeremorph
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 104, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 14, 'CON': 18, 'INT': 18, 'WIS': 15, 'CHAR': 14, 'armor_class': 15, 'alignment': 'typically Lawful Evil Armor Class  15 (natural armor) Hit Points  104 (11d10 + 44) Speed  40 ft. STR 18 (+4) DEX 14 (+2) CON 18 (+4) INT 18 (+4) WIS 15 (+2) CHA 14 (+2) Saving Throws  Int +7', 'legendary': False, 'size': 'Large', 'type': 'Aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

