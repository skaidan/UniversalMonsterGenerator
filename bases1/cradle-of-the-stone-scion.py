# bases1/cradle-of-the-stone-scion.py
"""
CradleOfTheStoneScion creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cradle-of-the-stone-scion
"""
from creature_base import GlobalCreatureBaseClass


class CradleOfTheStoneScion(GlobalCreatureBaseClass):
    """
    Gargantuan Elemental creature - CradleOfTheStoneScion
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 455, 'min_level': 1, 'level': 1, 'STR': 26, 'DEX': 15, 'CON': 24, 'INT': 11, 'WIS': 18, 'CHAR': 10, 'armor_class': 20, 'alignment': 'typically Neutral Armor Class  20 (natural armor) Hit Points  455 (26d20 + 182) Speed  40 ft. STR 26 (+8) DEX 15 (+2) CON 24 (+7) INT 11 (+0) WIS 18 (+4) CHA 10 (+0) Saving Throws  Wis +11', 'legendary': False, 'size': 'Gargantuan', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

