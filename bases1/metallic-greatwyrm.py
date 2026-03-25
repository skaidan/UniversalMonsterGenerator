# bases1/metallic-greatwyrm.py
"""
MetallicGreatwyrm creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=metallic-greatwyrm
"""
from creature_base import GlobalCreatureBaseClass


class MetallicGreatwyrm(GlobalCreatureBaseClass):
    """
    Gargantuan Dragon (Metallic) creature - MetallicGreatwyrm
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 565, 'min_level': 1, 'level': 1, 'STR': 30, 'DEX': 16, 'CON': 29, 'INT': 21, 'WIS': 22, 'CHAR': 30, 'armor_class': 22, 'alignment': 'typically Lawful Good Armor Class  22 (natural armor) Hit Points  565 (29d20 + 261) Speed  60 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'Dragon (Metallic)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

