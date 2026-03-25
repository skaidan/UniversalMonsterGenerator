# bases1/hobgoblin-warlord.py
"""
HobgoblinWarlord creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hobgoblin-warlord
"""
from creature_base import GlobalCreatureBaseClass


class HobgoblinWarlord(GlobalCreatureBaseClass):
    """
    Medium humanoid (Goblinoid) creature - HobgoblinWarlord
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 97, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 14, 'CON': 16, 'INT': 14, 'WIS': 11, 'CHAR': 15, 'armor_class': 20, 'alignment': 'lawful evil Armor Class  20 (plate', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Goblinoid)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['martial_advantage', 'multiattack', 'longsword', 'shield_bash', 'javelin', 'leadership_(recharges_after_a_short_or_long_rest)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def martial_advantage(self) -> str:
        """Once per turn, the hobgoblin can deal an extra 14 (4d6) damage to a creature it hits with a weapon attack if that creature is within 5 feet of an ally of the hobgoblin that isn't incapacitated."""
        return "Once per turn, the hobgoblin can deal an extra 14 (4d6) damage to a creature it hits with a weapon attack if that creature is within 5 feet of an ally of the hobgoblin that isn't incapacitated."

    def multiattack_attack(self) -> str:
        """The hobgoblin makes three melee attacks. Alternatively, it can make two ranged attacks with its javelins."""
        return 'The hobgoblin makes three melee attacks. Alternatively, it can make two ranged attacks with its javelins.'

    def longsword_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) slashing damage, or 8 (1d10 + 3) slashing damage if used with two hands."""
        return 'Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) slashing damage, or 8 (1d10 + 3) slashing damage if used with two hands.'

    def shield_bash_attack(self) -> str:
        """Melee Weapon Attack: +9 to hit, reach 5 ft., one creature. Hit: 5 (1d4 + 3) bludgeoning damage. If the target is Large or smaller, it must succeed on a DC 14 Strength saving throw or be knocked prone."""
        return 'Melee Weapon Attack: +9 to hit, reach 5 ft., one creature. Hit: 5 (1d4 + 3) bludgeoning damage. If the target is Large or smaller, it must succeed on a DC 14 Strength saving throw or be knocked prone.'

    def javelin_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +9 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 6 (1d6 + 3) piercing damage."""
        return 'Melee or Ranged Weapon Attack: +9 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 6 (1d6 + 3) piercing damage.'

    def leadership_(recharges_after_a_short_or_long_rest)_attack(self) -> str:
        """For 1 minute, the hobgoblin can utter a special command or warning whenever a nonhostile creature that it can see within 30 feet of it makes an attack roll or a saving throw. The creature can add a d4 to its roll provided it can hear and understand the hobgoblin. A creature can benefit from only one Leadership die at a time. This effect ends if the hobgoblin is incapacitated."""
        return 'For 1 minute, the hobgoblin can utter a special command or warning whenever a nonhostile creature that it can see within 30 feet of it makes an attack roll or a saving throw. The creature can add a d4 to its roll provided it can hear and understand the hobgoblin. A creature can benefit from only one Leadership die at a time. This effect ends if the hobgoblin is incapacitated.'

