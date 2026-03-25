# bases1/bael.py
"""
Bael creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bael
"""
from creature_base import GlobalCreatureBaseClass


class Bael(GlobalCreatureBaseClass):
    """
    Large Fiend (Devil) creature - Bael
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 189, 'min_level': 1, 'level': 1, 'STR': 24, 'DEX': 17, 'CON': 20, 'INT': 21, 'WIS': 24, 'CHAR': 24, 'armor_class': 18, 'alignment': 'Lawful Evil Armor Class  18 (plate) Hit Points  189 (18d10 + 90) Speed  30 ft. STR 24 (+7) DEX 17 (+3) CON 20 (+5) INT 21 (+5) WIS 24 (+7) CHA 24 (+7) Saving Throws  Dex +9', 'legendary': False, 'size': 'Large', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

