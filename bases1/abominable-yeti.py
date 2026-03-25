# bases1/abominable-yeti.py
"""
AbominableYeti creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=abominable-yeti
"""
from creature_base import GlobalCreatureBaseClass


class AbominableYeti(GlobalCreatureBaseClass):
    """
    Huge monstrosity creature - AbominableYeti
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 137, 'min_level': 1, 'level': 1, 'STR': 24, 'DEX': 10, 'CON': 22, 'INT': 9, 'WIS': 13, 'CHAR': 9, 'armor_class': 15, 'alignment': 'chaotic evil Armor Class  15 (natural armor) Hit Points  137 (11d12 + 66) Speed  40 ft.', 'legendary': False, 'size': 'Huge', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['fear_of_fire', 'multiattack', 'claw', 'chilling_gaze', 'cold_breath_(recharge_6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def fear_of_fire(self) -> str:
        """If the yeti takes fire damage, it has disadvantage on attack rolls and ability checks until the end of its next turn.Keen Smell. The yeti has advantage on Wisdom (Perception) checks that rely on smell"""
        return 'If the yeti takes fire damage, it has disadvantage on attack rolls and ability checks until the end of its next turn.Keen Smell. The yeti has advantage on Wisdom (Perception) checks that rely on smell'

    def multiattack_attack(self) -> str:
        """The yeti can use its Chilling Gaze and makes two claw attacks."""
        return 'The yeti can use its Chilling Gaze and makes two claw attacks.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 14 (2d6 + 7) slashing damage plus 7 (2d6) cold damage."""
        return 'Melee Weapon Attack: +11 to hit, reach 5 ft., one target. Hit: 14 (2d6 + 7) slashing damage plus 7 (2d6) cold damage.'

    def chilling_gaze_attack(self) -> str:
        """The yeti targets one creature it can see within 30 feet of it. If the target can see the yeti, the target must succeed on a DC 18 Constitution saving throw against this magic or take 21 (6d6) cold damage and then be paralyzed for 1 minute, unless it is immune to cold damage. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If the target's saving throw is successful, or if the effect ends on it, the target is immune to this yeti's gaze for 1 hour."""
        return "The yeti targets one creature it can see within 30 feet of it. If the target can see the yeti, the target must succeed on a DC 18 Constitution saving throw against this magic or take 21 (6d6) cold damage and then be paralyzed for 1 minute, unless it is immune to cold damage. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If the target's saving throw is successful, or if the effect ends on it, the target is immune to this yeti's gaze for 1 hour."

    def cold_breath_(recharge_6)_attack(self) -> str:
        """The yeti exhales a 30-foot cone of frigid air. Each creature in that area must make a DC 18 Constitution saving throw, taking 45 (10d8) cold damage on a failed save, or half as much damage on a successful one."""
        return 'The yeti exhales a 30-foot cone of frigid air. Each creature in that area must make a DC 18 Constitution saving throw, taking 45 (10d8) cold damage on a failed save, or half as much damage on a successful one.'

