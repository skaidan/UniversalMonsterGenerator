# bases1/stone-golem.py
"""
StoneGolem creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=stone-golem
"""
from creature_base import GlobalCreatureBaseClass


class StoneGolem(GlobalCreatureBaseClass):
    """
    Large construct creature - StoneGolem
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 178, 'min_level': 1, 'level': 1, 'STR': 22, 'DEX': 9, 'CON': 20, 'INT': 3, 'WIS': 11, 'CHAR': 1, 'armor_class': 17, 'alignment': 'unaligned Armor Class  17 (natural armor) Hit Points  178 (17d10 + 85) Speed  30 ft. STR 22 (+6) DEX 9 (-1) CON 20 (+5) INT 3 (-4) WIS 11 (+0) CHA 1 (-5) Damage Immunities  poison', 'legendary': False, 'size': 'Large', 'type': 'construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['immutable_form', 'multiattack', 'slam', 'slow_(recharge_5-6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def immutable_form(self) -> str:
        """The golem is immune to any spell or effect that would alter its form.Magic Resistance. The golem has advantage on saving throws against spells and other magical effects.Magic Weapons. The golem's weap"""
        return "The golem is immune to any spell or effect that would alter its form.Magic Resistance. The golem has advantage on saving throws against spells and other magical effects.Magic Weapons. The golem's weap"

    def multiattack_attack(self) -> str:
        """The golem makes two slam attacks."""
        return 'The golem makes two slam attacks.'

    def slam_attack(self) -> str:
        """Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 19 (3d8 + 6) bludgeoning damage."""
        return 'Melee Weapon Attack: +10 to hit, reach 5 ft., one target. Hit: 19 (3d8 + 6) bludgeoning damage.'

    def slow_(recharge_5-6)_attack(self) -> str:
        """The golem targets one or more creatures it can see within 10 feet of it. Each target must make a DC 17 Wisdom saving throw against this magic. On a failed save, a target can't use reactions, its speed is halved, and it can't make more than one attack on its turn. In addition, the target can take either an action or a bonus action on its turn, not both. These effects last for 1 minute. A target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return "The golem targets one or more creatures it can see within 10 feet of it. Each target must make a DC 17 Wisdom saving throw against this magic. On a failed save, a target can't use reactions, its speed is halved, and it can't make more than one attack on its turn. In addition, the target can take either an action or a bonus action on its turn, not both. These effects last for 1 minute. A target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."

