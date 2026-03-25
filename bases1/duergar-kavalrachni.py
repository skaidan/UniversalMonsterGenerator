# bases1/duergar-kavalrachni.py
"""
DuergarKavalrachni creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=duergar-kavalrachni
"""
from creature_base import GlobalCreatureBaseClass


class DuergarKavalrachni(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Dwarf) creature - DuergarKavalrachni
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 26, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 11, 'CON': 14, 'INT': 11, 'WIS': 10, 'CHAR': 9, 'armor_class': 16, 'alignment': 'any alignment Armor Class  16 (scale mail', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Dwarf)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

