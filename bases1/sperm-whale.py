# bases1/sperm-whale.py
"""
SpermWhale creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=sperm-whale
"""
from creature_base import GlobalCreatureBaseClass


class SpermWhale(GlobalCreatureBaseClass):
    """
    Gargantuan beast creature - SpermWhale
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 189, 'min_level': 1, 'level': 1, 'STR': 26, 'DEX': 8, 'CON': 17, 'INT': 3, 'WIS': 12, 'CHAR': 5, 'armor_class': 13, 'alignment': 'unaligned Armor Class  13 (natural armor) Hit Points  189 (14d20 + 42) Speed  0 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

