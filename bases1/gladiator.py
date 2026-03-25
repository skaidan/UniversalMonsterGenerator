# bases1/gladiator.py
"""
Gladiator creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gladiator
"""
from creature_base import GlobalCreatureBaseClass


class Gladiator(GlobalCreatureBaseClass):
    """
    Medium humanoid (any race) creature - Gladiator
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 112, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 15, 'CON': 16, 'INT': 10, 'WIS': 12, 'CHAR': 15, 'armor_class': 16, 'alignment': 'any alignment Armor Class  16 (studded leather', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (any race)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['brave', 'multiattack', 'spear', 'shield_bash']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def brave(self) -> str:
        """The gladiator has advantage on saving throws against being frightened.Brute. A melee weapon deals one extra die of its damage when the gladiator hits with it (included in the attack)."""
        return 'The gladiator has advantage on saving throws against being frightened.Brute. A melee weapon deals one extra die of its damage when the gladiator hits with it (included in the attack).'

    def multiattack_attack(self) -> str:
        """The gladiator makes three melee attacks or two ranged attacks."""
        return 'The gladiator makes three melee attacks or two ranged attacks.'

    def spear_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +7 to hit, reach 5 ft. and range 20/60 ft., one target. Hit: 11 (2d6 + 4) piercing damage, or 13 (2d8 + 4) piercing damage if used with two hands to make a melee attack."""
        return 'Melee or Ranged Weapon Attack: +7 to hit, reach 5 ft. and range 20/60 ft., one target. Hit: 11 (2d6 + 4) piercing damage, or 13 (2d8 + 4) piercing damage if used with two hands to make a melee attack.'

    def shield_bash_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one creature. Hit: 9 (2d4 + 4) bludgeoning damage. If the target is a Medium or smaller creature, it must succeed on a DC 15 Strength saving throw or be knocked prone."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one creature. Hit: 9 (2d4 + 4) bludgeoning damage. If the target is a Medium or smaller creature, it must succeed on a DC 15 Strength saving throw or be knocked prone.'

