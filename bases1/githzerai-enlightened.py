# bases1/githzerai-enlightened.py
"""
GithzeraiEnlightened creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=githzerai-enlightened
"""
from creature_base import GlobalCreatureBaseClass


class GithzeraiEnlightened(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Gith) creature - GithzeraiEnlightened
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 112, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 19, 'CON': 16, 'INT': 17, 'WIS': 19, 'CHAR': 13, 'armor_class': 18, 'alignment': 'any alignment Armor Class  18 (psychic defense) Hit Points  112 (15d8 + 45) Speed  40 ft. STR 14 (+2) DEX 19 (+4) CON 16 (+3) INT 17 (+3) WIS 19 (+4) CHA 13 (+1) Saving Throws  Str +6', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Gith)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

