# bases1/centaur.py
"""
Centaur creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=centaur
"""
from creature_base import GlobalCreatureBaseClass


class Centaur(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - Centaur
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 45, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 14, 'CON': 14, 'INT': 9, 'WIS': 13, 'CHAR': 11, 'armor_class': 12, 'alignment': 'neutral good Armor Class  12 Hit Points  45 (6d10 + 12) Speed  50 ft. STR 18 (+4) DEX 14 (+2) CON 14 (+2) INT 9 (-1) WIS 13 (+1) CHA 11 (+0) Skills  Athletics +6', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['charge', 'multiattack', 'pike', 'hooves', 'longbow']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def charge(self) -> str:
        """If the centaur moves at least 30 feet straight toward a target and then hits it with a pike attack on the same turn, the target takes an extra 10 (3d6) piercing damage."""
        return 'If the centaur moves at least 30 feet straight toward a target and then hits it with a pike attack on the same turn, the target takes an extra 10 (3d6) piercing damage.'

    def multiattack_attack(self) -> str:
        """The centaur makes two attacks: one with its pike and one with its hooves or two with its longbow."""
        return 'The centaur makes two attacks: one with its pike and one with its hooves or two with its longbow.'

    def pike_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 9 (1d10 + 4) piercing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 9 (1d10 + 4) piercing damage.'

    def hooves_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage.'

    def longbow_attack(self) -> str:
        """Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage."""
        return 'Ranged Weapon Attack: +4 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage.'

