# bases1/orc-blade-of-ilneval.py
"""
OrcBladeOfIlneval creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=orc-blade-of-ilneval
"""
from creature_base import GlobalCreatureBaseClass


class OrcBladeOfIlneval(GlobalCreatureBaseClass):
    """
    Medium humanoid (Orc) creature - OrcBladeOfIlneval
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 60, 'min_level': 1, 'level': 1, 'STR': 17, 'DEX': 11, 'CON': 17, 'INT': 10, 'WIS': 12, 'CHAR': 14, 'armor_class': 18, 'alignment': 'chaotic evil Armor Class  18 (chain mail', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Orc)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['aggressive', 'multiattack', 'longsword', 'javelin', 'ilnevals_command_(recharge_4–6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def aggressive(self) -> str:
        """As a bonus action, the orc can move up to its speed toward a hostile creature that it can see.Foe Smiter of Ilneval. The orc deals an extra die of damage when it hits with a longsword attack (included"""
        return 'As a bonus action, the orc can move up to its speed toward a hostile creature that it can see.Foe Smiter of Ilneval. The orc deals an extra die of damage when it hits with a longsword attack (included'

    def multiattack_attack(self) -> str:
        """The orc makes two melee attacks with its longsword or two ranged attacks with its javelins. If Ilneval's Command is available to use, the orc can use it after these attacks."""
        return "The orc makes two melee attacks with its longsword or two ranged attacks with its javelins. If Ilneval's Command is available to use, the orc can use it after these attacks."

    def longsword_attack(self) -> str:
        """Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 12 (2d8 + 3) slashing damage, or 14 (2d10 + 3) slashing damage when used with two hands."""
        return 'Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 12 (2d8 + 3) slashing damage, or 14 (2d10 + 3) slashing damage when used with two hands.'

    def javelin_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 6 (1d6 + 3) piercing damage."""
        return 'Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 6 (1d6 + 3) piercing damage.'

    def ilnevals_command_(recharge_4–6)_attack(self) -> str:
        """Up to three allied orcs within 120 feet of this orc that can hear it can use their reactions to each make one weapon attack."""
        return 'Up to three allied orcs within 120 feet of this orc that can hear it can use their reactions to each make one weapon attack.'

