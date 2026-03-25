# bases1/homunculus-servant.py
"""
HomunculusServant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=homunculus-servant
"""
from creature_base import GlobalCreatureBaseClass


class HomunculusServant(GlobalCreatureBaseClass):
    """
    Tiny construct creature - HomunculusServant
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 10, 'min_level': 1, 'level': 1, 'STR': 4, 'DEX': 15, 'CON': 12, 'INT': 10, 'WIS': 10, 'CHAR': 7, 'armor_class': 13, 'alignment': '- Armor Class  13 (natural armor) Hit Points  1 + your Intelligence modifier + your artificer level (the homunculus has a number of Hit Dice [d4s] equal to your artificer level) Speed  20 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['evasion', 'force_strike']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def evasion(self) -> str:
        """If the homunculus is subjected to an effect that allows it to make a Dexterity saving throw to take only half damage, it instead takes no damage if it succeeds on the saving throw, and only half damag"""
        return 'If the homunculus is subjected to an effect that allows it to make a Dexterity saving throw to take only half damage, it instead takes no damage if it succeeds on the saving throw, and only half damag'

    def force_strike_attack(self) -> str:
        """Ranged Weapon Attack: your spell attack modifier to hit, range 30 ft., one target you can see. Hit: 1d4 + PB force damage."""
        return 'Ranged Weapon Attack: your spell attack modifier to hit, range 30 ft., one target you can see. Hit: 1d4 + PB force damage.'

