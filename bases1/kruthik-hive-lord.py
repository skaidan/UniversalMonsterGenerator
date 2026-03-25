# bases1/kruthik-hive-lord.py
"""
KruthikHiveLord creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=kruthik-hive-lord
"""
from creature_base import GlobalCreatureBaseClass


class KruthikHiveLord(GlobalCreatureBaseClass):
    """
    Large Monstrosity creature - KruthikHiveLord
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 102, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 16, 'CON': 17, 'INT': 10, 'WIS': 14, 'CHAR': 10, 'armor_class': 20, 'alignment': 'unaligned Armor Class  20 (natural armor) Hit Points  102 (12d10 + 36) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'Monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

