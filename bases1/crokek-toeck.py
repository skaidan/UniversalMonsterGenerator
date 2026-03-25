# bases1/crokek-toeck.py
"""
CrokekToeck creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=crokek-toeck
"""
from creature_base import GlobalCreatureBaseClass


class CrokekToeck(GlobalCreatureBaseClass):
    """
    Gargantuan fiend (Demon) creature - CrokekToeck
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 297, 'min_level': 1, 'level': 1, 'STR': 28, 'DEX': 10, 'CON': 24, 'INT': 6, 'WIS': 10, 'CHAR': 13, 'armor_class': 15, 'alignment': 'chaotic evil Armor Class  15 (natural armor) Hit Points  297 (17d20 + 119) Speed  60 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'fiend (Demon)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

