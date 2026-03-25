# bases1/storm-herald.py
"""
StormHerald creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=storm-herald
"""
from creature_base import GlobalCreatureBaseClass


class StormHerald(GlobalCreatureBaseClass):
    """
    Huge Aberration creature - StormHerald
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 287, 'min_level': 1, 'level': 1, 'STR': 27, 'DEX': 14, 'CON': 22, 'INT': 24, 'WIS': 18, 'CHAR': 18, 'armor_class': 16, 'alignment': 'typically Lawful Evil Armor Class  16 (natural armor) Hit Points  287 (23d12 + 138) Speed  50 ft.', 'legendary': False, 'size': 'Huge', 'type': 'Aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

