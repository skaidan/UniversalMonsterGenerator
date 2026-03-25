# bases1/giff.py
"""
Giff creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giff
"""
from creature_base import GlobalCreatureBaseClass


class Giff(GlobalCreatureBaseClass):
    """
    Medium Humanoid creature - Giff
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 60, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 14, 'CON': 17, 'INT': 11, 'WIS': 12, 'CHAR': 12, 'armor_class': 16, 'alignment': "any alignment Armor Class  16 (breastplate) Hit Points  60 (8d8 + 24) Speed  30 ft. STR 18 (+4) DEX 14 (+2) CON 17 (+3) INT 11 (+0) WIS 12 (+1) CHA 12 (+1) Senses  passive Perception 11 Languages  Common Challenge  3 (700 XP) \xa0 \xa0  Proficiency Bonus  +2 Firearms Knowledge . The giff's mastery of its weapons enables it to ignore the loading property of muskets and pistols. Headfirst Charge . The giff can try to knock a creature over; if the giff moves at least 20 feet in a straight line and ends within 5 feet of a Large or smaller creature", 'legendary': False, 'size': 'Medium', 'type': 'Humanoid', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['firearms_knowledge', 'multiattack', 'longsword', 'musket', 'pistol', 'fragmentation_grenade_(1/day)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def firearms_knowledge(self) -> str:
        """The giff's mastery of its weapons enables it to ignore the loading property of muskets and pistols.Headfirst Charge. The giff can try to knock a creature over; if the giff moves at least 20 feet in a """
        return "The giff's mastery of its weapons enables it to ignore the loading property of muskets and pistols.Headfirst Charge. The giff can try to knock a creature over; if the giff moves at least 20 feet in a "

    def multiattack_attack(self) -> str:
        """The giff makes two Longsword, Musket, or Pistol attacks."""
        return 'The giff makes two Longsword, Musket, or Pistol attacks.'

    def longsword_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) slashing damage, or 9 (1d10 + 4) slashing damage if used with two hands."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 8 (1d8 + 4) slashing damage, or 9 (1d10 + 4) slashing damage if used with two hands.'

    def musket_attack(self) -> str:
        """Ranged Weapon Attack: +4 to hit, range 40/120 ft., one target. Hit: 8 (1d12 + 2) piercing damage."""
        return 'Ranged Weapon Attack: +4 to hit, range 40/120 ft., one target. Hit: 8 (1d12 + 2) piercing damage.'

    def pistol_attack(self) -> str:
        """Ranged Weapon Attack: +4 to hit, range 30/90 ft., one target. Hit: 7 (1d10 + 2) piercing damage."""
        return 'Ranged Weapon Attack: +4 to hit, range 30/90 ft., one target. Hit: 7 (1d10 + 2) piercing damage.'

    def fragmentation_grenade_(1/day)_attack(self) -> str:
        """The giff throws a grenade up to 60 feet, and the grenade explodes in a 20-foot-radius sphere. Each creature in that area must make a DC 15 Dexterity saving throw, taking 17 (5d6) piercing damage on a failed save, or half as much damage on a successful one."""
        return 'The giff throws a grenade up to 60 feet, and the grenade explodes in a 20-foot-radius sphere. Each creature in that area must make a DC 15 Dexterity saving throw, taking 17 (5d6) piercing damage on a failed save, or half as much damage on a successful one.'

