# bases1/cradle-of-the-fire-scion.py
"""
CradleOfTheFireScion creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=cradle-of-the-fire-scion
"""
from creature_base import GlobalCreatureBaseClass


class CradleOfTheFireScion(GlobalCreatureBaseClass):
    """
    Gargantuan Elemental creature - CradleOfTheFireScion
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 555, 'min_level': 1, 'level': 1, 'STR': 28, 'DEX': 12, 'CON': 27, 'INT': 12, 'WIS': 20, 'CHAR': 17, 'armor_class': 20, 'alignment': 'typically Lawful Evil Armor Class  20 (natural armor) Hit Points  555 (30d20 + 240) Speed  40 ft. STR 28 (+9) DEX 12 (+1) CON 27 (+8) INT 12 (+1) WIS 20 (+5) CHA 17 (+3) Damage Resistances  cold', 'legendary': False, 'size': 'Gargantuan', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

