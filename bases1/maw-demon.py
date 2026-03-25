# bases1/maw-demon.py
"""
MawDemon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=maw-demon
"""
from creature_base import GlobalCreatureBaseClass


class MawDemon(GlobalCreatureBaseClass):
    """
    Medium Fiend (Demon) creature - MawDemon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 33, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 8, 'CON': 13, 'INT': 5, 'WIS': 8, 'CHAR': 5, 'armor_class': 13, 'alignment': 'typically Chaotic Evil Armor Class  13 (natural armor) Hit Points  33 (6d8 + 6) Speed  30 ft. STR 14 (+2) DEX 8 (-1) CON 13 (+1) INT 5 (-3) WIS 8 (-1) CHA 5 (-3) Damage Resistances  cold', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

