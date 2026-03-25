# bases1/chromatic-greatwyrm.py
"""
ChromaticGreatwyrm creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=chromatic-greatwyrm
"""
from creature_base import GlobalCreatureBaseClass


class ChromaticGreatwyrm(GlobalCreatureBaseClass):
    """
    Gargantuan Dragon (Chromatic) creature - ChromaticGreatwyrm
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 533, 'min_level': 1, 'level': 1, 'STR': 30, 'DEX': 14, 'CON': 30, 'INT': 21, 'WIS': 20, 'CHAR': 26, 'armor_class': 22, 'alignment': 'typically Chaotic Evil Armor Class  22 (natural armor) Hit Points  533 (26d20 + 260) Speed  60 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'Dragon (Chromatic)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

