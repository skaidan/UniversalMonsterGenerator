# bases1/bel.py
"""
Bel creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=bel
"""
from creature_base import GlobalCreatureBaseClass


class Bel(GlobalCreatureBaseClass):
    """
    Large Fiend (Devil) creature - Bel
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 364, 'min_level': 1, 'level': 1, 'STR': 28, 'DEX': 14, 'CON': 26, 'INT': 25, 'WIS': 19, 'CHAR': 26, 'armor_class': 19, 'alignment': 'Lawful Evil Armor Class  19 (natural armor) Hit Points  364 (27d10 + 216) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

