# bases1/myconid-sprout.py
"""
MyconidSprout creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=myconid-sprout
"""
from creature_base import GlobalCreatureBaseClass


class MyconidSprout(GlobalCreatureBaseClass):
    """
    Small plant creature - MyconidSprout
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 7, 'min_level': 1, 'level': 1, 'STR': 8, 'DEX': 10, 'CON': 10, 'INT': 8, 'WIS': 11, 'CHAR': 5, 'armor_class': 10, 'alignment': 'lawful neutral Armor Class  10 Hit Points  7 (2d6) Speed  10 ft. STR 8 (-1) DEX 10 (+0) CON 10 (+0) INT 8 (-1) WIS 11 (+0) CHA 5 (-3) Senses  darkvision 120 ft.', 'legendary': False, 'size': 'Small', 'type': 'plant', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['distress_spores', 'fist', 'rapport_spores_(3/day)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def distress_spores(self) -> str:
        """When the myconid takes damage, all other myconids within 240 feet of it can sense its pain.Sun Sickness. While in sunlight, the myconid has disadvantage on ability checks, attack rolls, and saving thr"""
        return 'When the myconid takes damage, all other myconids within 240 feet of it can sense its pain.Sun Sickness. While in sunlight, the myconid has disadvantage on ability checks, attack rolls, and saving thr'

    def fist_attack(self) -> str:
        """Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 1 (1d4 - 1) bludgeoning damage plus 2 (1d4) poison damage."""
        return 'Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 1 (1d4 - 1) bludgeoning damage plus 2 (1d4) poison damage.'

    def rapport_spores_(3/day)_attack(self) -> str:
        """A 10-foot radius of spores extends from the myconid. These spores can go around corners and affect only creatures with an Intelligence of 2 or higher that aren't undead, constructs, or elementals. Affected creatures can communicate telepathically with one another while they are within 30 feet of each other. The effect lasts for 1 hour."""
        return "A 10-foot radius of spores extends from the myconid. These spores can go around corners and affect only creatures with an Intelligence of 2 or higher that aren't undead, constructs, or elementals. Affected creatures can communicate telepathically with one another while they are within 30 feet of each other. The effect lasts for 1 hour."

