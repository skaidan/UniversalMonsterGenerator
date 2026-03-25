# bases1/iron-consul.py
"""
IronConsul creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=iron-consul
"""
from creature_base import GlobalCreatureBaseClass


class IronConsul(GlobalCreatureBaseClass):
    """
    Medium humanoid (Human) creature - IronConsul
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 45, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 11, 'CON': 16, 'INT': 12, 'WIS': 15, 'CHAR': 16, 'armor_class': 16, 'alignment': 'lawful evil Armor Class  16 (chain mail) Hit Points  45 (6d8 + 18) Speed  30 ft. STR 17 (+3) DEX 11 (+0) CON 16 (+3) INT 12 (+1) WIS 15 (+2) CHA 16 (+3) Saving Throws  Wis +4 Skills  Intimidation +5', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Human)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

