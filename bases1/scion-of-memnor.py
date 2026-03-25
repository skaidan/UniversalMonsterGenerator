# bases1/scion-of-memnor.py
"""
ScionOfMemnor creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=scion-of-memnor
"""
from creature_base import GlobalCreatureBaseClass


class ScionOfMemnor(GlobalCreatureBaseClass):
    """
    Gargantuan Giant (Titan) creature - ScionOfMemnor
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 656, 'min_level': 1, 'level': 1, 'STR': 30, 'DEX': 18, 'CON': 30, 'INT': 24, 'WIS': 22, 'CHAR': 26, 'armor_class': 20, 'alignment': 'typically Chaotic Neutral Armor Class  20 (natural armor) Hit Points  656 (32d20 + 320) Speed  60 ft.', 'legendary': False, 'size': 'Gargantuan', 'type': 'Giant (Titan)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

