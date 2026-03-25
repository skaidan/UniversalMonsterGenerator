# bases1/velociraptor.py
"""
Velociraptor creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=velociraptor
"""
from creature_base import GlobalCreatureBaseClass


class Velociraptor(GlobalCreatureBaseClass):
    """
    Tiny Beast (Dinosaur) creature - Velociraptor
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 10, 'min_level': 1, 'level': 1, 'STR': 6, 'DEX': 14, 'CON': 13, 'INT': 4, 'WIS': 12, 'CHAR': 6, 'armor_class': 13, 'alignment': "unaligned Armor Class  13 (natural armor) Hit Points  10 (3d4 + 3) Speed  30 ft. STR 6 (-2) DEX 14 (+2) CON 13 (+1) INT 4 (-3) WIS 12 (+1) CHA 6 (-2) Skills  Perception +3 Senses  passive Perception 13 Languages  — Challenge  1/4 (50 XP) \xa0 \xa0  Proficiency Bonus  +2 Pack Tactics . The velociraptor has advantage on an attack roll against a creature if at least one of the velociraptor's allies is within 5 feet of the creature and the ally isn't incapacitated. Actions Multiattack . The velociraptor makes one Bite attack and one Claw attack. Bite .  Melee Weapon Attack : +4 to hit", 'legendary': False, 'size': 'Tiny', 'type': 'Beast (Dinosaur)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['pack_tactics', 'multiattack', 'bite', 'claw']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def pack_tactics(self) -> str:
        """The velociraptor has advantage on an attack roll against a creature if at least one of the velociraptor's allies is within 5 feet of the creature and the ally isn't incapacitated."""
        return "The velociraptor has advantage on an attack roll against a creature if at least one of the velociraptor's allies is within 5 feet of the creature and the ally isn't incapacitated."

    def multiattack_attack(self) -> str:
        """The velociraptor makes one Bite attack and one Claw attack."""
        return 'The velociraptor makes one Bite attack and one Claw attack.'

    def bite_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 5 (1d6 + 2) piercing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 5 (1d6 + 2) piercing damage.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) slashing damage.'

