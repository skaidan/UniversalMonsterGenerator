# bases1/death-giant-shrouded-one.py
"""
DeathGiantShroudedOne creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=death-giant-shrouded-one
"""
from creature_base import GlobalCreatureBaseClass


class DeathGiantShroudedOne(GlobalCreatureBaseClass):
    """
    Huge Giant (Wizard) creature - DeathGiantShroudedOne
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 195, 'min_level': 1, 'level': 1, 'STR': 27, 'DEX': 14, 'CON': 20, 'INT': 23, 'WIS': 16, 'CHAR': 16, 'armor_class': 12, 'alignment': 'any alignment Armor Class  12 (15 with  mage armor ) Hit Points  195 (17d12 + 85) Speed  40 ft. STR 27 (+8) DEX 14 (+2) CON 20 (+5) INT 23 (+6) WIS 16 (+3) CHA 16 (+3) Saving Throws  Con +10', 'legendary': False, 'size': 'Huge', 'type': 'Giant (Wizard)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

