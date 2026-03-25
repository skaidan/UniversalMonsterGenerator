# bases1/duergar-mind-master.py
"""
DuergarMindMaster creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=duergar-mind-master
"""
from creature_base import GlobalCreatureBaseClass


class DuergarMindMaster(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Dwarf) creature - DuergarMindMaster
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 39, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 17, 'CON': 14, 'INT': 15, 'WIS': 10, 'CHAR': 12, 'armor_class': 14, 'alignment': 'any alignment Armor Class  14 (leather armor) Hit Points  39 (6d8 + 12) Speed  25 ft. STR 11 (+0) DEX 17 (+3) CON 14 (+2) INT 15 (+2) WIS 10 (+0) CHA 12 (+1) Saving Throws  Wis +2 Skills  Perception +2', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Dwarf)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

