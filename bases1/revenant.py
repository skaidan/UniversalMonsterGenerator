# bases1/revenant.py
"""
Revenant creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=revenant
"""
from creature_base import GlobalCreatureBaseClass


class Revenant(GlobalCreatureBaseClass):
    """
    Medium undead creature - Revenant
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 136, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 14, 'CON': 18, 'INT': 13, 'WIS': 16, 'CHAR': 18, 'armor_class': 13, 'alignment': 'neutral Armor Class  13 (leather armor) Hit Points  136 (16d8 + 64) Speed  30 ft. STR 18 (+4) DEX 14 (+2) CON 18 (+4) INT 13 (+1) WIS 16 (+3) CHA 18 (+4) Saving Throws  Str +7', 'legendary': False, 'size': 'Medium', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['regeneration', 'multiattack', 'fist', 'vengeful_glare']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def regeneration(self) -> str:
        """The revenant regains 10 hit points at the start of its turn. If the revenant takes fire or radiant damage, this trait doesn't function at the start of the revenant's next turn. The revenant's body is """
        return "The revenant regains 10 hit points at the start of its turn. If the revenant takes fire or radiant damage, this trait doesn't function at the start of the revenant's next turn. The revenant's body is "

    def multiattack_attack(self) -> str:
        """The revenant makes two fist attacks."""
        return 'The revenant makes two fist attacks.'

    def fist_attack(self) -> str:
        """Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage. If the target is a creature against which the revenant has sworn vengeance, the target takes an extra 14 (4d6) bludgeoning damage. Instead of dealing damage, the revenant can grapple the target (escape DC 14) provided the target is Large or smaller."""
        return 'Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage. If the target is a creature against which the revenant has sworn vengeance, the target takes an extra 14 (4d6) bludgeoning damage. Instead of dealing damage, the revenant can grapple the target (escape DC 14) provided the target is Large or smaller.'

    def vengeful_glare_attack(self) -> str:
        """The revenant targets one creature it can see within 30 feet of it and against which it has sworn vengeance. The target must make a DC 15 Wisdom saving throw. On a failure, the target is paralyzed until the revenant deals damage to it, or until the end of the revenant's next turn. When the paralysis ends, the target is frightened of the revenant for 1 minute. The frightened target can repeat the saving throw at the end of each of its turns, with disadvantage if it can see the revenant, ending the frightened condition on itself on a success."""
        return "The revenant targets one creature it can see within 30 feet of it and against which it has sworn vengeance. The target must make a DC 15 Wisdom saving throw. On a failure, the target is paralyzed until the revenant deals damage to it, or until the end of the revenant's next turn. When the paralysis ends, the target is frightened of the revenant for 1 minute. The frightened target can repeat the saving throw at the end of each of its turns, with disadvantage if it can see the revenant, ending the frightened condition on itself on a success."

