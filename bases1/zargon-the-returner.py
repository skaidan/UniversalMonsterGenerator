# bases1/zargon-the-returner.py
"""
ZargonTheReturner creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=zargon-the-returner
"""
from creature_base import GlobalCreatureBaseClass


class ZargonTheReturner(GlobalCreatureBaseClass):
    """
    Huge Aberration creature - ZargonTheReturner
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 253, 'min_level': 1, 'level': 1, 'STR': 22, 'DEX': 10, 'CON': 20, 'INT': 14, 'WIS': 18, 'CHAR': 18, 'armor_class': 18, 'alignment': 'Lawful Evil Armor Class  18 (natural armor) Hit Points  253 (22d12 + 110) Speed  40 ft.', 'legendary': False, 'size': 'Huge', 'type': 'Aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

