# bases1/fury-of-kostchtchie.py
"""
FuryOfKostchtchie creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fury-of-kostchtchie
"""
from creature_base import GlobalCreatureBaseClass


class FuryOfKostchtchie(GlobalCreatureBaseClass):
    """
    Huge Fiend (Demon) creature - FuryOfKostchtchie
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 216, 'min_level': 1, 'level': 1, 'STR': 26, 'DEX': 10, 'CON': 25, 'INT': 10, 'WIS': 12, 'CHAR': 11, 'armor_class': 16, 'alignment': 'typically Chaotic Evil Armor Class  16 (natural armor) Hit Points  216 (16d12 + 112) Speed  40 ft. STR 26 (+8) DEX 10 (+0) CON 25 (+7) INT 10 (+0) WIS 12 (+1) CHA 11 (+0) Saving Throws  Con +12', 'legendary': False, 'size': 'Huge', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

