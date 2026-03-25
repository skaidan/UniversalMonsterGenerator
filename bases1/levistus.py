# bases1/levistus.py
"""
Levistus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=levistus
"""
from creature_base import GlobalCreatureBaseClass


class Levistus(GlobalCreatureBaseClass):
    """
    Medium Fiend (Devil) creature - Levistus
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 336, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 26, 'CON': 22, 'INT': 25, 'WIS': 28, 'CHAR': 26, 'armor_class': 23, 'alignment': 'Lawful Evil Armor Class  23 (natural armor) Hit Points  336 (32d8 + 192) Speed  0 ft. STR 19 (+4) DEX 26 (+8) CON 22 (+6) INT 25 (+7) WIS 28 (+9) CHA 26 (+8) Saving Throws  Dex +16', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

