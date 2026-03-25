# bases1/giant-scorpion.py
"""
GiantScorpion creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=giant-scorpion
"""
from creature_base import GlobalCreatureBaseClass


class GiantScorpion(GlobalCreatureBaseClass):
    """
    Large beast creature - GiantScorpion
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 52, 'min_level': 1, 'level': 1, 'STR': 15, 'DEX': 13, 'CON': 15, 'INT': 1, 'WIS': 9, 'CHAR': 3, 'armor_class': 15, 'alignment': 'unaligned Armor Class  15 (natural armor) Hit Points  52 (7d10 + 14) Speed  40 ft. STR 15 (+2) DEX 13 (+1) CON 15 (+2) INT 1 (-5) WIS 9 (-1) CHA 3 (-4) Senses  blindsight 60 ft.', 'legendary': False, 'size': 'Large', 'type': 'beast', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['multiattack', 'claw', 'sting']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def multiattack_attack(self) -> str:
        """The scorpion makes three attacks: two with its claws and one with its sting."""
        return 'The scorpion makes three attacks: two with its claws and one with its sting.'

    def claw_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) bludgeoning damage, and the target is grappled (escape DC 12). The scorpion has two claws, each of which can grapple only one target."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) bludgeoning damage, and the target is grappled (escape DC 12). The scorpion has two claws, each of which can grapple only one target.'

    def sting_attack(self) -> str:
        """Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 7 (1d10 + 2) piercing damage, and the target must make a DC 12 Constitution saving throw, taking 22 (4d10) poison damage on a failed save, or half as much damage on a successful one."""
        return 'Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 7 (1d10 + 2) piercing damage, and the target must make a DC 12 Constitution saving throw, taking 22 (4d10) poison damage on a failed save, or half as much damage on a successful one.'

