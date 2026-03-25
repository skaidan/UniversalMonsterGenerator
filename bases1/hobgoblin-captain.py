# bases1/hobgoblin-captain.py
"""
HobgoblinCaptain creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hobgoblin-captain
"""
from creature_base import GlobalCreatureBaseClass


class HobgoblinCaptain(GlobalCreatureBaseClass):
    """
    Medium humanoid (Goblinoid) creature - HobgoblinCaptain
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 39, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 14, 'CON': 14, 'INT': 12, 'WIS': 10, 'CHAR': 13, 'armor_class': 17, 'alignment': 'lawful evil Armor Class  17 (half plate) Hit Points  39 (6d8 + 12) Speed  30 ft. STR 15 (+2) DEX 14 (+2) CON 14 (+2) INT 12 (+1) WIS 10 (+0) CHA 13 (+1) Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Medium', 'type': 'humanoid (Goblinoid)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['martial_advantage', 'multiattack', 'greatsword', 'javelin', 'leadership_(recharges_after_a_short_or_long_rest)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def martial_advantage(self) -> str:
        """Once per turn, the hobgoblin can deal an extra 10 (3d6) damage to a creature it hits with a weapon attack if that creature is within 5 feet of an ally of the hobgoblin that isn't incapacitated."""
        return "Once per turn, the hobgoblin can deal an extra 10 (3d6) damage to a creature it hits with a weapon attack if that creature is within 5 feet of an ally of the hobgoblin that isn't incapacitated."

    def multiattack_attack(self) -> str:
        """The hobgoblin makes two greatsword attacks."""
        return 'The hobgoblin makes two greatsword attacks.'

    def greatsword_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (2d6 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (2d6 + 2) piercing damage.'

    def javelin_attack(self) -> str:
        """Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Melee or Ranged Weapon Attack: +4 to hit, reach 5 ft. or range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage.'

    def leadership_(recharges_after_a_short_or_long_rest)_attack(self) -> str:
        """For 1 minute, the hobgoblin can utter a special command or warning whenever a nonhostile creature that it can see within 30 feet of it makes an attack roll or a saving throw. The creature can add a d4 to its roll provided it can hear and understand the hobgoblin. A creature can benefit from only one Leadership die at a time. This effect ends if the hobgoblin is incapacitated."""
        return 'For 1 minute, the hobgoblin can utter a special command or warning whenever a nonhostile creature that it can see within 30 feet of it makes an attack roll or a saving throw. The creature can add a d4 to its roll provided it can hear and understand the hobgoblin. A creature can benefit from only one Leadership die at a time. This effect ends if the hobgoblin is incapacitated.'

