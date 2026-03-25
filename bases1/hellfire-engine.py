# bases1/hellfire-engine.py
"""
HellfireEngine creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hellfire-engine
"""
from creature_base import GlobalCreatureBaseClass


class HellfireEngine(GlobalCreatureBaseClass):
    """
    Huge Construct creature - HellfireEngine
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 216, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 16, 'CON': 24, 'INT': 2, 'WIS': 10, 'CHAR': 1, 'armor_class': 18, 'alignment': 'typically Lawful Evil Armor Class  18 (natural armor) Hit Points  216 (16d12 + 112) Speed  40 ft. STR 20 (+5) DEX 16 (+3) CON 24 (+7) INT 2 (-4) WIS 10 (+0) CHA 1 (-5) Saving Throws  Dex +8', 'legendary': False, 'size': 'Huge', 'type': 'Construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

