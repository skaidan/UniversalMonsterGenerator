# bases1/dragon-chosen.py
"""
DragonChosen creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dragon-chosen
"""
from creature_base import GlobalCreatureBaseClass


class DragonChosen(GlobalCreatureBaseClass):
    """
    Medium Humanoid creature - DragonChosen
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 45, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 18, 'CON': 14, 'INT': 10, 'WIS': 13, 'CHAR': 14, 'armor_class': 17, 'alignment': 'any alignment Armor Class  17 (natural armor) Hit Points  45 (7d8 + 14) Speed  30 ft. STR 18 (+4) DEX 18 (+4) CON 14 (+2) INT 10 (+0) WIS 13 (+1) CHA 14 (+2) Saving Throws  Str +6', 'legendary': False, 'size': 'Medium', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

