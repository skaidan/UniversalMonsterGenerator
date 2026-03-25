# bases1/fierna.py
"""
Fierna creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fierna
"""
from creature_base import GlobalCreatureBaseClass


class Fierna(GlobalCreatureBaseClass):
    """
    Medium Fiend (Devil) creature - Fierna
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 367, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 25, 'CON': 22, 'INT': 22, 'WIS': 22, 'CHAR': 29, 'armor_class': 20, 'alignment': 'Lawful Evil Armor Class  20 (natural armor) Hit Points  367 (35d8 + 210) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

