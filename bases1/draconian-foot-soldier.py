# bases1/draconian-foot-soldier.py
"""
DraconianFootSoldier creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=draconian-foot-soldier
"""
from creature_base import GlobalCreatureBaseClass


class DraconianFootSoldier(GlobalCreatureBaseClass):
    """
    Medium monstrosity creature - DraconianFootSoldier
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 11, 'CON': 13, 'INT': 8, 'WIS': 8, 'CHAR': 10, 'armor_class': 14, 'alignment': 'any alignment Armor Class  14 (natural armor) Hit Points  22 (4d8 + 4) Speed  30 ft. STR 13 (+1) DEX 11 (+0) CON 13 (+1) INT 8 (-1) WIS 8 (-1) CHA 10 (+0) Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Medium', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

