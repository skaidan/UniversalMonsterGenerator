# bases1/sprite.py
"""
Sprite creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=sprite
"""
from creature_base import GlobalCreatureBaseClass


class Sprite(GlobalCreatureBaseClass):
    """
    Tiny fey creature - Sprite
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 2, 'min_level': 1, 'level': 1, 'STR': 3, 'DEX': 18, 'CON': 10, 'INT': 14, 'WIS': 13, 'CHAR': 11, 'armor_class': 15, 'alignment': 'neutral good Armor Class  15 (leather armor) Hit Points  2 (1d4) Speed  10 ft.', 'legendary': False, 'size': 'Tiny', 'type': 'fey', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['longsword', 'shortbow', 'heart_sight', 'invisibility']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def longsword_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 1 slashing damage."""
        return 'Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 1 slashing damage.'

    def shortbow_attack(self) -> str:
        """Ranged Weapon Attack: +6 to hit, range 40/160 ft., one target. Hit: 1 piercing damage, and the target must succeed on a DC 10 Constitution saving throw or become poisoned for 1 minute. If its saving throw result is 5 or lower, the poisoned target falls unconscious for the same duration, or until it takes damage or another creature takes an action to shake it awake."""
        return 'Ranged Weapon Attack: +6 to hit, range 40/160 ft., one target. Hit: 1 piercing damage, and the target must succeed on a DC 10 Constitution saving throw or become poisoned for 1 minute. If its saving throw result is 5 or lower, the poisoned target falls unconscious for the same duration, or until it takes damage or another creature takes an action to shake it awake.'

    def heart_sight_attack(self) -> str:
        """The sprite touches a creature and magically knows the creature's current emotional state. If the target fails a DC 10 Charisma saving throw, the sprite also knows the creature's alignment. Celestials, fiends, and undead automatically fail the saving throw."""
        return "The sprite touches a creature and magically knows the creature's current emotional state. If the target fails a DC 10 Charisma saving throw, the sprite also knows the creature's alignment. Celestials, fiends, and undead automatically fail the saving throw."

    def invisibility_attack(self) -> str:
        """The sprite magically turns invisible until it attacks or casts a spell, or until its concentration ends (as if concentrating on a spell). Any equipment the sprite wears or carries is invisible with it."""
        return 'The sprite magically turns invisible until it attacks or casts a spell, or until its concentration ends (as if concentrating on a spell). Any equipment the sprite wears or carries is invisible with it.'

