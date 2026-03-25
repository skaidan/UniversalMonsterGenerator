# bases1/gargantua.py
"""
Gargantua creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gargantua
"""
from creature_base import GlobalCreatureBaseClass


class Gargantua(GlobalCreatureBaseClass):
    """
    Gargantuan Aberration creature - Gargantua
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 388, 'min_level': 1, 'level': 1, 'STR': 27, 'DEX': 10, 'CON': 26, 'INT': 9, 'WIS': 16, 'CHAR': 18, 'armor_class': 17, 'alignment': 'typically Chaotic Neutral Armor Class  17 (natural armor) Hit Points  388 (21d20 + 168) Speed  60 ft. STR 27 (+8) DEX 10 (+0) CON 26 (+8) INT 9 (-1) WIS 16 (+3) CHA 18 (+4) Saving Throws  Dex +7', 'legendary': False, 'size': 'Gargantuan', 'type': 'Aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

