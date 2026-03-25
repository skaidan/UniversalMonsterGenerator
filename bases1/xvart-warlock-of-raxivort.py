# bases1/xvart-warlock-of-raxivort.py
"""
XvartWarlockOfRaxivort creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=xvart-warlock-of-raxivort
"""
from creature_base import GlobalCreatureBaseClass


class XvartWarlockOfRaxivort(GlobalCreatureBaseClass):
    """
    Small Monstrosity creature - XvartWarlockOfRaxivort
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 8, 'DEX': 14, 'CON': 12, 'INT': 8, 'WIS': 11, 'CHAR': 12, 'armor_class': 12, 'alignment': 'typically Chaotic Evil Armor Class  12 Hit Points  22 (5d6 + 5) Speed  30 ft. STR 8 (-1) DEX 14 (+2) CON 12 (+1) INT 8 (-1) WIS 11 (+0) CHA 12 (+1) Skills  Stealth +3 Senses  darkvision 30 ft.', 'legendary': False, 'size': 'Small', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

