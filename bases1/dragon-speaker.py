# bases1/dragon-speaker.py
"""
DragonSpeaker creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dragon-speaker
"""
from creature_base import GlobalCreatureBaseClass


class DragonSpeaker(GlobalCreatureBaseClass):
    """
    Small Humanoid creature - DragonSpeaker
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 36, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 14, 'CON': 12, 'INT': 13, 'WIS': 11, 'CHAR': 17, 'armor_class': 13, 'alignment': 'any alignment Armor Class  13 (leather armor) Hit Points  36 (8d6 + 8) Speed  30 ft. STR 10 (+0) DEX 14 (+2) CON 12 (+1) INT 13 (+1) WIS 11 (+0) CHA 17 (+3) Saving Throws  Dex +4', 'legendary': False, 'size': 'Small', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

