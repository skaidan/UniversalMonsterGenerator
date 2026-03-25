# bases1/iggwilv-the-witch-queen.py
"""
IggwilvTheWitchQueen creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=iggwilv-the-witch-queen
"""
from creature_base import GlobalCreatureBaseClass


class IggwilvTheWitchQueen(GlobalCreatureBaseClass):
    """
    Medium fey (Wizard) creature - IggwilvTheWitchQueen
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 255, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 18, 'CON': 18, 'INT': 27, 'WIS': 12, 'CHAR': 23, 'armor_class': 19, 'alignment': 'chaotic neutral Armor Class  19 ( robe of the archmagi ) Hit Points  255 (30d8 + 120) Speed  30 ft. STR 10 (+0) DEX 18 (+4) CON 18 (+4) INT 27 (+8) WIS 12 (+1) CHA 23 (+6) Saving Throws  Int +14', 'legendary': False, 'size': 'Medium', 'type': 'fey (Wizard)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

