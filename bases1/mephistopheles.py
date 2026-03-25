# bases1/mephistopheles.py
"""
Mephistopheles creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=mephistopheles
"""
from creature_base import GlobalCreatureBaseClass


class Mephistopheles(GlobalCreatureBaseClass):
    """
    Large Fiend (Devil) creature - Mephistopheles
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 460, 'min_level': 1, 'level': 1, 'STR': 22, 'DEX': 23, 'CON': 22, 'INT': 30, 'WIS': 28, 'CHAR': 26, 'armor_class': 21, 'alignment': 'Lawful Evil Armor Class  21 (natural armor) Hit Points  460 (40d10 + 240) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'Fiend (Devil)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

