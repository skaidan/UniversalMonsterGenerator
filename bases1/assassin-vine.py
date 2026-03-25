# bases1/assassin-vine.py
"""
AssassinVine creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=assassin-vine
"""
from creature_base import GlobalCreatureBaseClass


class AssassinVine(GlobalCreatureBaseClass):
    """
    Large plant creature - AssassinVine
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 85, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 10, 'CON': 16, 'INT': 1, 'WIS': 10, 'CHAR': 1, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 (natural armor) Hit Points  85 (10d10 + 30) Speed  5 ft.', 'legendary': False, 'size': 'Large', 'type': 'plant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

