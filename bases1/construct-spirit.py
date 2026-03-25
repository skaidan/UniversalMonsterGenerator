# bases1/construct-spirit.py
"""
ConstructSpirit creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=construct-spirit
"""
from creature_base import GlobalCreatureBaseClass


class ConstructSpirit(GlobalCreatureBaseClass):
    """
    Medium construct creature - ConstructSpirit
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 10, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 10, 'CON': 18, 'INT': 14, 'WIS': 11, 'CHAR': 5, 'armor_class': 13, 'alignment': '- Armor Class  13 + the level of the spell (natural armor) Hit Points  40 + 15 for each spell level above 4th Speed  30 ft. STR 18 (+4) DEX 10 (+0) CON 18 (+4) INT 14 (+2) WIS 11 (+0) CHA 5 (-3) Damage Resistances  poison Condition Immunities  charmed', 'legendary': False, 'size': 'Medium', 'type': 'construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

