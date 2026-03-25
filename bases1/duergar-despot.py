# bases1/duergar-despot.py
"""
DuergarDespot creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=duergar-despot
"""
from creature_base import GlobalCreatureBaseClass


class DuergarDespot(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Dwarf) creature - DuergarDespot
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 119, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 5, 'CON': 19, 'INT': 15, 'WIS': 14, 'CHAR': 13, 'armor_class': 21, 'alignment': 'any alignment Armor Class  21 (natural armor) Hit Points  119 (14d8 + 56) Speed  25 ft. STR 20 (+5) DEX 5 (-3) CON 19 (+4) INT 15 (+2) WIS 14 (+2) CHA 13 (+1) Saving Throws  Con +8', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Dwarf)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

