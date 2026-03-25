# bases1/choldrith.py
"""
Choldrith creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=choldrith
"""
from creature_base import GlobalCreatureBaseClass


class Choldrith(GlobalCreatureBaseClass):
    """
    Medium Monstrosity (Cleric) creature - Choldrith
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 66, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 16, 'CON': 12, 'INT': 11, 'WIS': 14, 'CHAR': 10, 'armor_class': 15, 'alignment': 'typically Chaotic Evil Armor Class  15 (natural armor) Hit Points  66 (12d8 + 12) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Monstrosity (Cleric)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

