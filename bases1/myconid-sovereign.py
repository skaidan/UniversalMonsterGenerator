# bases1/myconid-sovereign.py
"""
MyconidSovereign creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=myconid-sovereign
"""
from creature_base import GlobalCreatureBaseClass


class MyconidSovereign(GlobalCreatureBaseClass):
    """
    Large plant creature - MyconidSovereign
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 60, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 10, 'CON': 14, 'INT': 13, 'WIS': 15, 'CHAR': 10, 'armor_class': 13, 'alignment': 'lawful neutral Armor Class  13 (natural armor) Hit Points  60 (8d10 + 16) Speed  30 ft. STR 12 (+1) DEX 10 (+0) CON 14 (+2) INT 13 (+1) WIS 15 (+2) CHA 10 (+0) Senses  darkvision 120 ft.', 'legendary': False, 'size': 'Large', 'type': 'plant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['distress_spores', 'multiattack', 'fist', 'animating_spores_(3/day)', 'hallucination_spores', 'pacifying_spores', 'rapport_spores']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def distress_spores(self) -> str:
        """When the myconid takes damage, all other myconids within 240 feet of it can sense its pain.Sun Sickness. While in sunlight, the myconid has disadvantage on ability checks, attack rolls, and saving thr"""
        return 'When the myconid takes damage, all other myconids within 240 feet of it can sense its pain.Sun Sickness. While in sunlight, the myconid has disadvantage on ability checks, attack rolls, and saving thr'

    def multiattack_attack(self) -> str:
        """The myconid uses either its Hallucination Spores or its Pacifying Spores, then makes a fist attack."""
        return 'The myconid uses either its Hallucination Spores or its Pacifying Spores, then makes a fist attack.'

    def fist_attack(self) -> str:
        """Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 8 (3d4 + 1) bludgeoning damage plus 7 (3d4) poison damage."""
        return 'Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 8 (3d4 + 1) bludgeoning damage plus 7 (3d4) poison damage.'

    def animating_spores_(3/day)_attack(self) -> str:
        """The myconid targets one corpse of a humanoid or a Large or smaller beast within 5 feet of it and releases spores at the corpse. In 24 hours, the corpse rises as a spore servant. The corpse stays animated for 1d4 + 1 weeks or until destroyed, and it can't be animated again in this way."""
        return "The myconid targets one corpse of a humanoid or a Large or smaller beast within 5 feet of it and releases spores at the corpse. In 24 hours, the corpse rises as a spore servant. The corpse stays animated for 1d4 + 1 weeks or until destroyed, and it can't be animated again in this way."

    def hallucination_spores_attack(self) -> str:
        """The myconid ejects spores at one creature it can see within 5 feet of it. The target must succeed on a DC 12 Constitution saving throw or be poisoned for 1 minute. The poisoned target is incapacitated while it hallucinates. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'The myconid ejects spores at one creature it can see within 5 feet of it. The target must succeed on a DC 12 Constitution saving throw or be poisoned for 1 minute. The poisoned target is incapacitated while it hallucinates. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

    def pacifying_spores_attack(self) -> str:
        """The myconid ejects spores at one creature it can see within 5 feet of it. The target must succeed on a DC 12 Constitution saving throw or be stunned for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'The myconid ejects spores at one creature it can see within 5 feet of it. The target must succeed on a DC 12 Constitution saving throw or be stunned for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

    def rapport_spores_attack(self) -> str:
        """A 30-foot radius of spores extends from the myconid. These spores can go around corners and affect only creatures with an Intelligence of 2 or higher that aren't undead, constructs, or elementals. Affected creatures can communicate telepathically with one another while they are within 30 feet of each other. The effect lasts for 1 hour."""
        return "A 30-foot radius of spores extends from the myconid. These spores can go around corners and affect only creatures with an Intelligence of 2 or higher that aren't undead, constructs, or elementals. Affected creatures can communicate telepathically with one another while they are within 30 feet of each other. The effect lasts for 1 hour."

