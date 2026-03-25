# bases1/orthon.py
"""
Orthon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=orthon
"""
from creature_base import GlobalCreatureBaseClass


class Orthon(GlobalCreatureBaseClass):
    """
    Large Fiend (Devil) creature - Orthon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 105, 'min_level': 1, 'level': 1, 'STR': 22, 'DEX': 16, 'CON': 21, 'INT': 15, 'WIS': 15, 'CHAR': 16, 'armor_class': 17, 'alignment': 'typically Lawful Evil Armor Class  17 (half plate) Hit Points  105 (10d10 + 50) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

