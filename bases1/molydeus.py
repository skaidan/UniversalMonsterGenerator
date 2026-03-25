# bases1/molydeus.py
"""
Molydeus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=molydeus
"""
from creature_base import GlobalCreatureBaseClass


class Molydeus(GlobalCreatureBaseClass):
    """
    Huge Fiend (Demon) creature - Molydeus
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 216, 'min_level': 1, 'level': 1, 'STR': 28, 'DEX': 22, 'CON': 25, 'INT': 21, 'WIS': 24, 'CHAR': 24, 'armor_class': 19, 'alignment': 'typically Chaotic Evil Armor Class  19 (natural armor) Hit Points  216 (16d12 + 112) Speed  40 ft. STR 28 (+9) DEX 22 (+6) CON 25 (+7) INT 21 (+5) WIS 24 (+7) CHA 24 (+7) Saving Throws  Str +16', 'legendary': False, 'size': 'Huge', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

