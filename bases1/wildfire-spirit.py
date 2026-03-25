# bases1/wildfire-spirit.py
"""
WildfireSpirit creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=wildfire-spirit
"""
from creature_base import GlobalCreatureBaseClass


class WildfireSpirit(GlobalCreatureBaseClass):
    """
    Small elemental creature - WildfireSpirit
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 10, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 14, 'CON': 14, 'INT': 13, 'WIS': 15, 'CHAR': 11, 'armor_class': 13, 'alignment': '- Armor Class  13 (natural armor) Hit Points  5 + five times your druid level Speed  30 ft.', 'legendary': False, 'size': 'Small', 'type': 'elemental', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

