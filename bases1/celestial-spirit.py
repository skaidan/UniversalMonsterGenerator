# bases1/celestial-spirit.py
"""
CelestialSpirit creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=celestial-spirit
"""
from creature_base import GlobalCreatureBaseClass


class CelestialSpirit(GlobalCreatureBaseClass):
    """
    Large celestial creature - CelestialSpirit
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 10, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 14, 'CON': 16, 'INT': 10, 'WIS': 14, 'CHAR': 16, 'armor_class': 11, 'alignment': '- Armor Class  11 + the level of the spell (natural armor) + 2 (Defender only) Hit Points  40 + 10 for each spell level above 5th Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'celestial', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

