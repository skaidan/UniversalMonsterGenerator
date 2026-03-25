# bases1/myconid-adult.py
"""
MyconidAdult creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=myconid-adult
"""
from creature_base import GlobalCreatureBaseClass


class MyconidAdult(GlobalCreatureBaseClass):
    """
    Medium plant creature - MyconidAdult
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 22, 'min_level': 1, 'level': 1, 'STR': 10, 'DEX': 10, 'CON': 12, 'INT': 10, 'WIS': 13, 'CHAR': 7, 'armor_class': 12, 'alignment': 'lawful neutral Armor Class  12 (natural armor) Hit Points  22 (4d8 + 4) Speed  20 ft. STR 10 (+0) DEX 10 (+0) CON 12 (+1) INT 10 (+0) WIS 13 (+1) CHA 7 (-2) Senses  darkvision 120 ft.', 'legendary': False, 'size': 'Medium', 'type': 'plant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['distress_spores', 'fist', 'pacifying_spores_(3/day)', 'rapport_spores']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def distress_spores(self) -> str:
        """When the myconid takes damage, all other myconids within 240 feet of it can sense its pain.Sun Sickness. While in sunlight, the myconid has disadvantage on ability checks, attack rolls, and saving thr"""
        return 'When the myconid takes damage, all other myconids within 240 feet of it can sense its pain.Sun Sickness. While in sunlight, the myconid has disadvantage on ability checks, attack rolls, and saving thr'

    def fist_attack(self) -> str:
        """Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 5 (2d4) bludgeoning damage plus 5 (2d4) poison damage."""
        return 'Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 5 (2d4) bludgeoning damage plus 5 (2d4) poison damage.'

    def pacifying_spores_(3/day)_attack(self) -> str:
        """The myconid ejects spores at one creature it can see within 5 feet of it. The target must succeed on a DC 11 Constitution saving throw or be stunned for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success."""
        return 'The myconid ejects spores at one creature it can see within 5 feet of it. The target must succeed on a DC 11 Constitution saving throw or be stunned for 1 minute. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.'

    def rapport_spores_attack(self) -> str:
        """A 20-foot radius of spores extends from the myconid. These spores can go around corners and affect only creatures with an Intelligence of 2 or higher that aren't undead, constructs, or elementals. Affected creatures can communicate telepathically with one another while they are within 30 feet of each other. The effect lasts for 1 hour."""
        return "A 20-foot radius of spores extends from the myconid. These spores can go around corners and affect only creatures with an Intelligence of 2 or higher that aren't undead, constructs, or elementals. Affected creatures can communicate telepathically with one another while they are within 30 feet of each other. The effect lasts for 1 hour."

