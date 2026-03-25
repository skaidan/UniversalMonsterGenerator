# bases1/echo-of-demogorgon.py
"""
EchoOfDemogorgon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=echo-of-demogorgon
"""
from creature_base import GlobalCreatureBaseClass


class EchoOfDemogorgon(GlobalCreatureBaseClass):
    """
    Large Fiend (Demon) creature - EchoOfDemogorgon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 85, 'min_level': 1, 'level': 1, 'STR': 22, 'DEX': 10, 'CON': 17, 'INT': 10, 'WIS': 12, 'CHAR': 14, 'armor_class': 14, 'alignment': 'typically Chaotic Evil Armor Class  14 (natural armor) Hit Points  85 (10d10 + 30) Speed  40 ft. STR 22 (+6) DEX 10 (+0) CON 17 (+3) INT 10 (+0) WIS 12 (+1) CHA 14 (+2) Saving Throws  Str +9', 'legendary': False, 'size': 'Large', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

