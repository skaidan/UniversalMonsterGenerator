# bases1/asmodeus.py
"""
Asmodeus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=asmodeus
"""
from creature_base import GlobalCreatureBaseClass


class Asmodeus(GlobalCreatureBaseClass):
    """
    Large Fiend (Devil) creature - Asmodeus
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 725, 'min_level': 1, 'level': 1, 'STR': 30, 'DEX': 21, 'CON': 28, 'INT': 25, 'WIS': 30, 'CHAR': 30, 'armor_class': 22, 'alignment': 'Lawful Evil Armor Class  22 (natural armor) Hit Points  725 (50d10 + 450) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

