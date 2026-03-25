# bases1/black-gauntlet-of-bane.py
"""
BlackGauntletOfBane creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=black-gauntlet-of-bane
"""
from creature_base import GlobalCreatureBaseClass


class BlackGauntletOfBane(GlobalCreatureBaseClass):
    """
    Medium humanoid (Human) creature - BlackGauntletOfBane
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 51, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 11, 'CON': 18, 'INT': 12, 'WIS': 15, 'CHAR': 18, 'armor_class': 16, 'alignment': 'lawful evil Armor Class  16 (chain mail) Hit Points  51 (6d8 + 24) Speed  30 ft. STR 18 (+4) DEX 11 (+0) CON 18 (+4) INT 12 (+1) WIS 15 (+2) CHA 18 (+4) Saving Throws  Wis +5 Skills  Intimidation +7', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Human)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

