# bases1/death-giant-reaper.py
"""
DeathGiantReaper creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=death-giant-reaper
"""
from creature_base import GlobalCreatureBaseClass


class DeathGiantReaper(GlobalCreatureBaseClass):
    """
    Huge Giant creature - DeathGiantReaper
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 172, 'min_level': 1, 'level': 1, 'STR': 27, 'DEX': 14, 'CON': 20, 'INT': 18, 'WIS': 16, 'CHAR': 16, 'armor_class': 18, 'alignment': 'any alignment Armor Class  18 (plate) Hit Points  172 (15d12 + 75) Speed  40 ft. STR 27 (+8) DEX 14 (+2) CON 20 (+5) INT 18 (+4) WIS 16 (+3) CHA 16 (+3) Saving Throws  Con +9', 'legendary': False, 'size': 'Huge', 'type': 'Giant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

