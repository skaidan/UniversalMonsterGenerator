# bases1/ancient-sea-serpent.py
"""
AncientSeaSerpent creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=ancient-sea-serpent
"""
from creature_base import GlobalCreatureBaseClass


class AncientSeaSerpent(GlobalCreatureBaseClass):
    """
    Gargantuan Dragon creature - AncientSeaSerpent
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 170, 'min_level': 1, 'level': 1, 'STR': 24, 'DEX': 15, 'CON': 20, 'INT': 13, 'WIS': 16, 'CHAR': 12, 'armor_class': 17, 'alignment': 'typically Neutral Armor Class  17 (natural armor) Hit Points  170 (11d20 + 55) Speed  20 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'Dragon', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

