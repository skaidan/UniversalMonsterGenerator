# bases1/cradle-of-the-hill-scion.py
"""
CradleOfTheHillScion creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cradle-of-the-hill-scion
"""
from creature_base import GlobalCreatureBaseClass


class CradleOfTheHillScion(GlobalCreatureBaseClass):
    """
    Gargantuan Elemental creature - CradleOfTheHillScion
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 402, 'min_level': 1, 'level': 1, 'STR': 25, 'DEX': 10, 'CON': 24, 'INT': 9, 'WIS': 16, 'CHAR': 10, 'armor_class': 19, 'alignment': 'typically Chaotic Evil Armor Class  19 (natural armor) Hit Points  402 (23d20 + 161) Speed  40 ft. STR 25 (+7) DEX 10 (+0) CON 24 (+7) INT 9 (-1) WIS 16 (+3) CHA 10 (+0) Saving Throws  Wis +10', 'legendary': False, 'size': 'Gargantuan', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

