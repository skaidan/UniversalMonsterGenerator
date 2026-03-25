# bases1/young-emerald-dragon.py
"""
YoungEmeraldDragon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=young-emerald-dragon
"""
from creature_base import GlobalCreatureBaseClass


class YoungEmeraldDragon(GlobalCreatureBaseClass):
    """
    Large dragon (Gem) creature - YoungEmeraldDragon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 142, 'min_level': 1, 'level': 1, 'STR': 21, 'DEX': 12, 'CON': 19, 'INT': 16, 'WIS': 14, 'CHAR': 16, 'armor_class': 17, 'alignment': 'typically Lawful Neutral Armor Class  17 (natural armor) Hit Points  142 (15d10 + 60) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'dragon (Gem)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

