# bases1/firbolg-primeval-warden.py
"""
FirbolgPrimevalWarden creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=firbolg-primeval-warden
"""
from creature_base import GlobalCreatureBaseClass


class FirbolgPrimevalWarden(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Druid) creature - FirbolgPrimevalWarden
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 65, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 14, 'CON': 14, 'INT': 12, 'WIS': 16, 'CHAR': 11, 'armor_class': 16, 'alignment': 'any alignment Armor Class  16 (hide armor', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Druid)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

