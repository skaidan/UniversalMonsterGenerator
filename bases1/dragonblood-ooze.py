# bases1/dragonblood-ooze.py
"""
DragonbloodOoze creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dragonblood-ooze
"""
from creature_base import GlobalCreatureBaseClass


class DragonbloodOoze(GlobalCreatureBaseClass):
    """
    Large Ooze creature - DragonbloodOoze
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 68, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 6, 'CON': 17, 'INT': 2, 'WIS': 12, 'CHAR': 10, 'armor_class': 14, 'alignment': 'unaligned Armor Class  14 (natural armor) Hit Points  68 (8d10 + 24) Speed  20 ft.', 'legendary': False, 'size': 'Large', 'type': 'Ooze', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

