# bases1/oinoloth.py
"""
Oinoloth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=oinoloth
"""
from creature_base import GlobalCreatureBaseClass


class Oinoloth(GlobalCreatureBaseClass):
    """
    Medium Fiend (Yugoloth) creature - Oinoloth
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 119, 'min_level': 1, 'level': 1, 'STR': 19, 'DEX': 17, 'CON': 18, 'INT': 17, 'WIS': 16, 'CHAR': 19, 'armor_class': 17, 'alignment': 'typically Neutral Evil Armor Class  17 (natural armor) Hit Points  119 (14d8 + 56) Speed  40 ft. STR 19 (+4) DEX 17 (+3) CON 18 (+4) INT 17 (+3) WIS 16 (+3) CHA 19 (+4) Saving Throws  Con +8', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Yugoloth)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

