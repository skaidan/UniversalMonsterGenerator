# bases1/leviathan.py
"""
Leviathan creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=leviathan
"""
from creature_base import GlobalCreatureBaseClass


class Leviathan(GlobalCreatureBaseClass):
    """
    Gargantuan Elemental creature - Leviathan
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 328, 'min_level': 1, 'level': 1, 'STR': 30, 'DEX': 24, 'CON': 30, 'INT': 2, 'WIS': 18, 'CHAR': 17, 'armor_class': 17, 'alignment': 'typically Neutral Armor Class  17 Hit Points  328 (16d20 + 160) Speed  40 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'Elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

