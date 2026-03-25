# bases1/dhergoloth.py
"""
Dhergoloth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=dhergoloth
"""
from creature_base import GlobalCreatureBaseClass


class Dhergoloth(GlobalCreatureBaseClass):
    """
    Medium Fiend (Yugoloth) creature - Dhergoloth
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 119, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 10, 'CON': 19, 'INT': 7, 'WIS': 10, 'CHAR': 9, 'armor_class': 15, 'alignment': 'typically Neutral Evil Armor Class  15 (natural armor) Hit Points  119 (14d8 + 56) Speed  30 ft. STR 17 (+3) DEX 10 (+0) CON 19 (+4) INT 7 (-2) WIS 10 (+0) CHA 9 (-1) Saving Throws  Str +6 Damage Resistances  cold', 'legendary': False, 'size': 'Medium', 'type': 'Fiend (Yugoloth)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

