# bases1/steel-defender.py
"""
SteelDefender creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=steel-defender
"""
from creature_base import GlobalCreatureBaseClass


class SteelDefender(GlobalCreatureBaseClass):
    """
    Medium construct creature - SteelDefender
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 10, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 12, 'CON': 14, 'INT': 4, 'WIS': 10, 'CHAR': 6, 'armor_class': 15, 'alignment': '- Armor Class  15 (natural armor) Hit Points  2 + your Intelligence modifier + five times your artificer level (the defender has a number of Hit Dice [d8s] equal to your artificer level) Speed  40 ft. STR 14 (+2) DEX 12 (+1) CON 14 (+2) INT 4 (-3) WIS 10 (+0) CHA 6 (-2) Saving Throws  Dex +1 plus PB', 'legendary': False, 'size': 'Medium', 'type': 'construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['vigilant', 'force-empowered_rend', 'repair_(3/day)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def vigilant(self) -> str:
        """The defender can't be surprised."""
        return "The defender can't be surprised."

    def force-empowered_rend_attack(self) -> str:
        """Melee Weapon Attack: your spell attack modifier to hit, reach 5 ft., one target you can see. Hit: 1d8 + PB force damage."""
        return 'Melee Weapon Attack: your spell attack modifier to hit, reach 5 ft., one target you can see. Hit: 1d8 + PB force damage.'

    def repair_(3/day)_attack(self) -> str:
        """The magical mechanisms inside the defender restore 2d8 + PB hit points to itself or to one construct or object within 5 feet of it."""
        return 'The magical mechanisms inside the defender restore 2d8 + PB hit points to itself or to one construct or object within 5 feet of it.'

