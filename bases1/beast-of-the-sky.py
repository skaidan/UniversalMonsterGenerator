# bases1/beast-of-the-sky.py
"""
BeastOfTheSky creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=beast-of-the-sky
"""
from creature_base import GlobalCreatureBaseClass


class BeastOfTheSky(GlobalCreatureBaseClass):
    """
    Small beast creature - BeastOfTheSky
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 10, 'min_level': 1, 'level': 1, 'STR': 6, 'DEX': 16, 'CON': 13, 'INT': 8, 'WIS': 14, 'CHAR': 11, 'armor_class': 13, 'alignment': '- Armor Class  13 + PB (natural armor) Hit Points  4 + four times your ranger level (the beast has a number of Hit Dice [d6s] equal to your ranger level) Speed  10 ft.', 'legendary': False, 'size': 'Small', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

