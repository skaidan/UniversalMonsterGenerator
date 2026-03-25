# bases1/scion-of-skoraeus.py
"""
ScionOfSkoraeus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=scion-of-skoraeus
"""
from creature_base import GlobalCreatureBaseClass


class ScionOfSkoraeus(GlobalCreatureBaseClass):
    """
    Gargantuan Giant (Titan) creature - ScionOfSkoraeus
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 444, 'min_level': 1, 'level': 1, 'STR': 29, 'DEX': 20, 'CON': 26, 'INT': 19, 'WIS': 24, 'CHAR': 14, 'armor_class': 19, 'alignment': 'typically Neutral Armor Class  19 (natural armor) Hit Points  444 (24d20 + 192) Speed  60 ft. STR 29 (+9) DEX 20 (+5) CON 26 (+8) INT 19 (+4) WIS 24 (+7) CHA 14 (+2) Saving Throws  Dex +12', 'legendary': False, 'size': 'Gargantuan', 'type': 'Giant (Titan)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

