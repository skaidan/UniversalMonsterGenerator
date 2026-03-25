# bases1/belial.py
"""
Belial creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=belial
"""
from creature_base import GlobalCreatureBaseClass


class Belial(GlobalCreatureBaseClass):
    """
    Medium Fiend (Devil) creature - Belial
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 420, 'min_level': 1, 'level': 1, 'STR': 25, 'DEX': 17, 'CON': 22, 'INT': 22, 'WIS': 22, 'CHAR': 29, 'armor_class': 21, 'alignment': 'Lawful Evil Armor Class  21 (natural armor) Hit Points  420 (40d8 + 240) Speed  30 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

