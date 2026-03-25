# bases1/armanite.py
"""
Armanite creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=armanite
"""
from creature_base import GlobalCreatureBaseClass


class Armanite(GlobalCreatureBaseClass):
    """
    Large Fiend (Demon) creature - Armanite
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 94, 'min_level': 1, 'level': 1, 'STR': 21, 'DEX': 18, 'CON': 21, 'INT': 8, 'WIS': 12, 'CHAR': 13, 'armor_class': 16, 'alignment': 'typically Chaotic Evil Armor Class  16 (natural armor) Hit Points  94 (9d10 + 45) Speed  60 ft. STR 21 (+5) DEX 18 (+4) CON 21 (+5) INT 8 (-1) WIS 12 (+1) CHA 13 (+1) Damage Resistances  cold', 'legendary': False, 'size': 'Large', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

