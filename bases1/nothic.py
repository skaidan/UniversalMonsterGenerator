# bases1/nothic.py
"""
Nothic creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=nothic
"""
from creature_base import GlobalCreatureBaseClass


class Nothic(GlobalCreatureBaseClass):
    """
    Medium aberration creature - Nothic
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 45, 'min_level': 1, 'level': 1, 'STR': 14, 'DEX': 16, 'CON': 16, 'INT': 13, 'WIS': 10, 'CHAR': 8, 'armor_class': 15, 'alignment': 'neutral evil Armor Class  15 (natural armor) Hit Points  45 (6d8 + 18) Speed  30 ft. STR 14 (+2) DEX 16 (+3) CON 16 (+3) INT 13 (+1) WIS 10 (+0) CHA 8 (-1) Skills  Arcana +3', 'legendary': False, 'size': 'Medium', 'type': 'aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['keen_sight', 'multiattack', 'claw', 'rotting_gaze', 'weird_insight']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def keen_sight(self) -> str:
        """The nothic has advantage on Wisdom (Perception) checks that rely on sight."""
        return 'The nothic has advantage on Wisdom (Perception) checks that rely on sight.'

    def multiattack_attack(self) -> str:
        """The nothic makes two claw attacks."""
        return 'The nothic makes two claw attacks.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage.'

    def rotting_gaze_attack(self) -> str:
        """The nothic targets one creature it can see within 30 feet of it. The target must succeed on a DC 12 Constitution saving throw against this magic or take 10 (3d6) necrotic damage."""
        return 'The nothic targets one creature it can see within 30 feet of it. The target must succeed on a DC 12 Constitution saving throw against this magic or take 10 (3d6) necrotic damage.'

    def weird_insight_attack(self) -> str:
        """The nothic targets one creature it can see within 30 feet of it. The target must contest its Charisma (Deception) check against the nothic's Wisdom (Insight) check. If the nothic wins, it magically learns one fact or secret about the target. The target automatically wins if it is immune to being charmed."""
        return "The nothic targets one creature it can see within 30 feet of it. The target must contest its Charisma (Deception) check against the nothic's Wisdom (Insight) check. If the nothic wins, it magically learns one fact or secret about the target. The target automatically wins if it is immune to being charmed."

