# bases1/unicorn.py
"""
Unicorn creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=unicorn
"""
from creature_base import GlobalCreatureBaseClass


class Unicorn(GlobalCreatureBaseClass):
    """
    Large celestial creature - Unicorn
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 67, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 14, 'CON': 15, 'INT': 11, 'WIS': 17, 'CHAR': 16, 'armor_class': 12, 'alignment': 'lawful good Armor Class  12 Hit Points  67 (9d10 + 18) Speed  50 ft. STR 18 (+4) DEX 14 (+2) CON 15 (+2) INT 11 (+0) WIS 17 (+3) CHA 16 (+3) Damage Immunities  poison Condition Immunities  charmed', 'legendary': False, 'size': 'Large', 'type': 'celestial', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['charge', 'multiattack', 'hooves', 'horn', 'healing_touch_(3/day)', 'teleport_(1/day)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def charge(self) -> str:
        """If the unicorn moves at least 20 feet straight toward a target and then hits it with a horn attack on the same turn, the target takes an extra 9 (2d8) piercing damage. If the target is a creature, it """
        return 'If the unicorn moves at least 20 feet straight toward a target and then hits it with a horn attack on the same turn, the target takes an extra 9 (2d8) piercing damage. If the target is a creature, it '

    def multiattack_attack(self) -> str:
        """The unicorn makes two attacks: one with its hooves and one with its horn."""
        return 'The unicorn makes two attacks: one with its hooves and one with its horn.'

    def hooves_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage.'

    def horn_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) piercing damage."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) piercing damage.'

    def healing_touch_(3/day)_attack(self) -> str:
        """The unicorn touches another creature with its horn. The target magically regains 11 (2d8 + 2) hit points. In addition, the touch removes all diseases and neutralizes all poisons afflicting the target."""
        return 'The unicorn touches another creature with its horn. The target magically regains 11 (2d8 + 2) hit points. In addition, the touch removes all diseases and neutralizes all poisons afflicting the target.'

    def teleport_(1/day)_attack(self) -> str:
        """The unicorn magically teleports itself and up to three willing creatures it can see within 5 feet of it, along with any equipment they are wearing or carrying, to a location the unicorn is familiar with, up to 1 mile away."""
        return 'The unicorn magically teleports itself and up to three willing creatures it can see within 5 feet of it, along with any equipment they are wearing or carrying, to a location the unicorn is familiar with, up to 1 mile away.'

