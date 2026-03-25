# bases1/skull-lasher-of-myrkul.py
"""
SkullLasherOfMyrkul creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=skull-lasher-of-myrkul
"""
from creature_base import GlobalCreatureBaseClass


class SkullLasherOfMyrkul(GlobalCreatureBaseClass):
    """
    Medium humanoid (Human) creature - SkullLasherOfMyrkul
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 32, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 14, 'CON': 15, 'INT': 16, 'WIS': 13, 'CHAR': 10, 'armor_class': 12, 'alignment': 'neutral evil Armor Class  12 Hit Points  32 (5d8 + 10) Speed  30 ft. STR 10 (+0) DEX 14 (+2) CON 15 (+2) INT 16 (+3) WIS 13 (+1) CHA 10 (+0) Saving Throws  Wis +3 Skills  Arcana +5', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Human)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

