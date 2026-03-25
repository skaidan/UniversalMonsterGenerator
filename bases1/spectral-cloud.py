# bases1/spectral-cloud.py
"""
SpectralCloud creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=spectral-cloud
"""
from creature_base import GlobalCreatureBaseClass


class SpectralCloud(GlobalCreatureBaseClass):
    """
    Huge Undead creature - SpectralCloud
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 189, 'min_level': 1, 'level': 1, 'STR': 24, 'DEX': 12, 'CON': 18, 'INT': 12, 'WIS': 17, 'CHAR': 16, 'armor_class': 11, 'alignment': 'typically Neutral Armor Class  11 Hit Points  189 (18d12 + 72) Speed  0 ft.', 'legendary': False, 'size': 'Huge', 'type': 'Undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

