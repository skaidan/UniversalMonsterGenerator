# bases1/deathlock-mastermind.py
"""
DeathlockMastermind creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=deathlock-mastermind
"""
from creature_base import GlobalCreatureBaseClass


class DeathlockMastermind(GlobalCreatureBaseClass):
    """
    Medium Undead (Warlock) creature - DeathlockMastermind
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 110, 'min_level': 1, 'level': 1, 'STR': 11, 'DEX': 16, 'CON': 12, 'INT': 15, 'WIS': 12, 'CHAR': 17, 'armor_class': 13, 'alignment': 'typically Neutral Evil Armor Class  13 (16 with  mage armor ) Hit Points  110 (20d8 + 20) Speed  30 ft. STR 11 (+0) DEX 16 (+3) CON 12 (+1) INT 15 (+2) WIS 12 (+1) CHA 17 (+3) Saving Throws  Int +5', 'legendary': False, 'size': 'Medium', 'type': 'Undead (Warlock)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

