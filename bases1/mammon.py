# bases1/mammon.py
"""
Mammon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mammon
"""
from creature_base import GlobalCreatureBaseClass


class Mammon(GlobalCreatureBaseClass):
    """
    Huge Fiend (Devil) creature - Mammon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 464, 'min_level': 1, 'level': 1, 'STR': 28, 'DEX': 17, 'CON': 26, 'INT': 22, 'WIS': 25, 'CHAR': 25, 'armor_class': 18, 'alignment': 'Lawful Evil Armor Class  18 (natural armor) Hit Points  464 (32d12 + 256) Speed  40 ft. STR 28 (+9) DEX 17 (+3) CON 26 (+8) INT 22 (+6) WIS 25 (+7) CHA 25 (+7) Saving Throws  Dex +11', 'legendary': False, 'size': 'Huge', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

