# bases1/githyanki-supreme-commander.py
"""
GithyankiSupremeCommander creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=githyanki-supreme-commander
"""
from creature_base import GlobalCreatureBaseClass


class GithyankiSupremeCommander(GlobalCreatureBaseClass):
    """
    Medium Humanoid (Gith) creature - GithyankiSupremeCommander
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 187, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 17, 'CON': 18, 'INT': 16, 'WIS': 16, 'CHAR': 18, 'armor_class': 18, 'alignment': 'any alignment Armor Class  18 (plate) Hit Points  187 (22d8 + 88) Speed  30 ft. STR 19 (+4) DEX 17 (+3) CON 18 (+4) INT 16 (+3) WIS 16 (+3) CHA 18 (+4) Saving Throws  Con +9', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid (Gith)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

