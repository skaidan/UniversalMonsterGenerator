# bases1/gem-greatwyrm.py
"""
GemGreatwyrm creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gem-greatwyrm
"""
from creature_base import GlobalCreatureBaseClass


class GemGreatwyrm(GlobalCreatureBaseClass):
    """
    Gargantuan Dragon (Gem) creature - GemGreatwyrm
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 507, 'min_level': 1, 'level': 1, 'STR': 28, 'DEX': 14, 'CON': 29, 'INT': 30, 'WIS': 24, 'CHAR': 25, 'armor_class': 21, 'alignment': 'typically Neutral Armor Class  21 (natural armor) Hit Points  507 (26d20 + 234) Speed  60 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'Dragon (Gem)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

