# bases1/maurezhi.py
"""
Maurezhi creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=maurezhi
"""
from creature_base import GlobalCreatureBaseClass


class Maurezhi(GlobalCreatureBaseClass):
    """
    Medium Fiend (Demon) creature - Maurezhi
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 88, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 17, 'CON': 12, 'INT': 11, 'WIS': 12, 'CHAR': 15, 'armor_class': 15, 'alignment': 'typically Chaotic Evil Armor Class  15 (natural armor) Hit Points  88 (16d8 + 16) Speed  30 ft. STR 14 (+2) DEX 17 (+3) CON 12 (+1) INT 11 (+0) WIS 12 (+1) CHA 15 (+2) Skills  Deception +5 Damage Resistances  cold', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

