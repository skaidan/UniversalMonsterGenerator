# bases1/wastrilith.py
"""
Wastrilith creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=wastrilith
"""
from creature_base import GlobalCreatureBaseClass


class Wastrilith(GlobalCreatureBaseClass):
    """
    Large Fiend (Demon) creature - Wastrilith
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 157, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 18, 'CON': 21, 'INT': 19, 'WIS': 12, 'CHAR': 14, 'armor_class': 18, 'alignment': 'typically Chaotic Evil Armor Class  18 (natural armor) Hit Points  157 (15d10 + 75) Speed  30 ft.', 'legendary': False, 'size': 'Large', 'type': 'Fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

