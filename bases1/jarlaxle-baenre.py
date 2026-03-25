# bases1/jarlaxle-baenre.py
"""
JarlaxleBaenre creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=jarlaxle-baenre
"""
from creature_base import GlobalCreatureBaseClass


class JarlaxleBaenre(GlobalCreatureBaseClass):
    """
    Medium humanoid (Elf) creature - JarlaxleBaenre
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 123, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 22, 'CON': 14, 'INT': 20, 'WIS': 16, 'CHAR': 19, 'armor_class': 24, 'alignment': 'chaotic neutral Armor Class  24 ( +3 leather armor', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Elf)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

