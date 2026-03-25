# bases1/mud-hulk.py
"""
MudHulk creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mud-hulk
"""
from creature_base import GlobalCreatureBaseClass


class MudHulk(GlobalCreatureBaseClass):
    """
    Large Elemental creature - MudHulk
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 68, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 8, 'CON': 16, 'INT': 5, 'WIS': 9, 'CHAR': 6, 'armor_class': 13, 'alignment': 'typically Chaotic Evil Armor Class  13 (natural armor) Hit Points  68 (8d10 + 24) Speed  40 ft. STR 16 (+3) DEX 8 (-1) CON 16 (+3) INT 5 (-3) WIS 9 (-1) CHA 6 (-2) Damage Resistances  acid Condition Immunities  exhaustion', 'legendary': False, 'size': 'Large', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

