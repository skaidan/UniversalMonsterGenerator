# bases1/yeti.py
"""
Yeti creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=yeti
"""
from creature_base import GlobalCreatureBaseClass


class Yeti(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - Yeti
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 51, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 13, 'CON': 16, 'INT': 8, 'WIS': 12, 'CHAR': 7, 'armor_class': 12, 'alignment': 'chaotic evil Armor Class  12 (natural armor) Hit Points  51 (6d10 + 18) Speed  40 ft.', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['fear_of_fire', 'multiattack', 'claw', 'chilling_gaze']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def fear_of_fire(self) -> str:
        """If the yeti takes fire damage, it has disadvantage on attack rolls and ability checks until the end of its next turn.Keen Smell. The yeti has advantage on Wisdom (Perception) checks that rely on smell"""
        return 'If the yeti takes fire damage, it has disadvantage on attack rolls and ability checks until the end of its next turn.Keen Smell. The yeti has advantage on Wisdom (Perception) checks that rely on smell'

    def multiattack_attack(self) -> str:
        """The yeti can use its Chilling Gaze and makes two claw attacks."""
        return 'The yeti can use its Chilling Gaze and makes two claw attacks.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) slashing damage plus 3 (1d6) cold damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 7 (1d6 + 4) slashing damage plus 3 (1d6) cold damage.'

    def chilling_gaze_attack(self) -> str:
        """The yeti targets one creature it can see within 30 feet of it. If the target can see the yeti, the target must succeed on a DC 13 Constitution saving throw against this magic or take 10 (3d6) cold damage and then be paralyzed for 1 minute, unless it is immune to cold damage. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If the target's saving throw is successful, or if the effect ends on it, the target is immune to the Chilling Gaze of all yetis (but not abominable yetis) for 1 hour."""
        return "The yeti targets one creature it can see within 30 feet of it. If the target can see the yeti, the target must succeed on a DC 13 Constitution saving throw against this magic or take 10 (3d6) cold damage and then be paralyzed for 1 minute, unless it is immune to cold damage. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. If the target's saving throw is successful, or if the effect ends on it, the target is immune to the Chilling Gaze of all yetis (but not abominable yetis) for 1 hour."

