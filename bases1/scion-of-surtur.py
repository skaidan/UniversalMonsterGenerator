# bases1/scion-of-surtur.py
"""
ScionOfSurtur creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=scion-of-surtur
"""
from creature_base import GlobalCreatureBaseClass


class ScionOfSurtur(GlobalCreatureBaseClass):
    """
    Gargantuan Giant (Titan) creature - ScionOfSurtur
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 546, 'min_level': 1, 'level': 1, 'STR': 30, 'DEX': 17, 'CON': 28, 'INT': 21, 'WIS': 24, 'CHAR': 20, 'armor_class': 20, 'alignment': 'typically Lawful Evil Armor Class  20 (natural armor) Hit Points  546 (28d20 + 252) Speed  60 ft. STR 30 (+10) DEX 17 (+3) CON 28 (+9) INT 21 (+5) WIS 24 (+7) CHA 20 (+5) Saving Throws  Dex +11', 'legendary': False, 'size': 'Gargantuan', 'type': 'Giant (Titan)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

