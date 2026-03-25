# bases1/moloch.py
"""
Moloch creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=moloch
"""
from creature_base import GlobalCreatureBaseClass


class Moloch(GlobalCreatureBaseClass):
    """
    Large Fiend (Devil) creature - Moloch
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 253, 'min_level': 1, 'level': 1, 'STR': 26, 'DEX': 19, 'CON': 22, 'INT': 21, 'WIS': 18, 'CHAR': 23, 'armor_class': 19, 'alignment': 'Lawful Evil Armor Class  19 (natural armor) Hit Points  253 (22d10 + 132) Speed  30 ft. STR 26 (+8) DEX 19 (+4) CON 22 (+6) INT 21 (+5) WIS 18 (+4) CHA 23 (+6) Saving Throws  Dex +11', 'legendary': False, 'size': 'Large', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

