# bases1/zuggtmoy.py
"""
Zuggtmoy creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=zuggtmoy
"""
from creature_base import GlobalCreatureBaseClass


class Zuggtmoy(GlobalCreatureBaseClass):
    """
    Large Fiend (Demon) creature - Zuggtmoy
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 304, 'min_level': 1, 'level': 1, 'STR': 22, 'DEX': 15, 'CON': 18, 'INT': 20, 'WIS': 19, 'CHAR': 24, 'armor_class': 18, 'alignment': 'Chaotic Evil Armor Class  18 (natural armor) Hit Points  304 (32d10 + 128) Speed  30 ft. STR 22 (+6) DEX 15 (+2) CON 18 (+4) INT 20 (+5) WIS 19 (+4) CHA 24 (+7) Saving Throws  Dex +9', 'legendary': False, 'size': 'Large', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

