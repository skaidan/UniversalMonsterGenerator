# bases1/neothelid.py
"""
Neothelid creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=neothelid
"""
from creature_base import GlobalCreatureBaseClass


class Neothelid(GlobalCreatureBaseClass):
    """
    Gargantuan Aberration creature - Neothelid
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 232, 'min_level': 1, 'level': 1, 'STR': 27, 'DEX': 7, 'CON': 21, 'INT': 3, 'WIS': 16, 'CHAR': 12, 'armor_class': 16, 'alignment': 'typically Chaotic Evil Armor Class  16 (natural armor) Hit Points  232 (15d20 + 75) Speed  30 ft. STR 27 (+8) DEX 7 (-2) CON 21 (+5) INT 3 (-4) WIS 16 (+3) CHA 12 (+1) Saving Throws  Int +1', 'legendary': False, 'size': 'Gargantuan', 'type': 'Aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

