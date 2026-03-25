# bases1/titivilus.py
"""
Titivilus creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=titivilus
"""
from creature_base import GlobalCreatureBaseClass


class Titivilus(GlobalCreatureBaseClass):
    """
    Medium Fiend (Devil) creature - Titivilus
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 150, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 22, 'CON': 17, 'INT': 24, 'WIS': 22, 'CHAR': 26, 'armor_class': 20, 'alignment': 'Lawful Evil Armor Class  20 (natural armor) Hit Points  150 (20d8 + 60) Speed  40 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

