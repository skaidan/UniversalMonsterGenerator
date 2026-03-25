# bases1/stone-cursed.py
"""
StoneCursed creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=stone-cursed
"""
from creature_base import GlobalCreatureBaseClass


class StoneCursed(GlobalCreatureBaseClass):
    """
    Medium Construct creature - StoneCursed
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 19, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 5, 'CON': 14, 'INT': 5, 'WIS': 8, 'CHAR': 7, 'armor_class': 17, 'alignment': 'typically Lawful Evil Armor Class  17 (natural armor) Hit Points  19 (3d8 + 6) Speed  10 ft. STR 16 (+3) DEX 5 (-3) CON 14 (+2) INT 5 (-3) WIS 8 (-1) CHA 7 (-2) Damage Vulnerabilities  bludgeoning Damage Immunities  poison Condition Immunities  charmed', 'legendary': False, 'size': 'Medium', 'type': 'Construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

