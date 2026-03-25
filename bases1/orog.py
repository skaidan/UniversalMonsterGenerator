# bases1/orog.py
"""
Orog creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=orog
"""
from creature_base import GlobalCreatureBaseClass


class Orog(GlobalCreatureBaseClass):
    """
    Medium humanoid (Orc) creature - Orog
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 42, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 12, 'CON': 18, 'INT': 12, 'WIS': 11, 'CHAR': 12, 'armor_class': 18, 'alignment': 'chaotic evil Armor Class  18 (plate) Hit Points  42 (5d8 + 20) Speed  30 ft. STR 18 (+4) DEX 12 (+1) CON 18 (+4) INT 12 (+1) WIS 11 (+0) CHA 12 (+1) Skills  Intimidation +5', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Orc)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['aggressive', 'multiattack', 'greataxe', 'javelin']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def aggressive(self) -> str:
        """As a bonus action, the orog can move up to its speed toward a hostile creature that it can see."""
        return 'As a bonus action, the orog can move up to its speed toward a hostile creature that it can see.'

    def multiattack_attack(self) -> str:
        """The orog makes two greataxe attacks."""
        return 'The orog makes two greataxe attacks.'

    def greataxe_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 10 (1d12 + 4) slashing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 10 (1d12 + 4) slashing damage.'

    def javelin_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 7 (1d6 + 4) piercing damage."""
        return 'Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 7 (1d6 + 4) piercing damage.'

