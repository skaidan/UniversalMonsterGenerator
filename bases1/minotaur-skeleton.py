# bases1/minotaur-skeleton.py
"""
MinotaurSkeleton creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=minotaur-skeleton
"""
from creature_base import GlobalCreatureBaseClass


class MinotaurSkeleton(GlobalCreatureBaseClass):
    """
    Large undead creature - MinotaurSkeleton
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 67, 'min_level': 1, 'level': 1, 'STR': 18, 'DEX': 11, 'CON': 15, 'INT': 6, 'WIS': 8, 'CHAR': 5, 'armor_class': 12, 'alignment': 'lawful evil Armor Class  12 (natural armor) Hit Points  67 (9d10 + 18) Speed  40 ft. STR 18 (+4) DEX 11 (+0) CON 15 (+2) INT 6 (-2) WIS 8 (-1) CHA 5 (-3) Damage Vulnerabilities  bludgeoning Damage Immunities  poison Condition Immunities  exhaustion', 'legendary': False, 'size': 'Large', 'type': 'undead', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['charge', 'greataxe', 'gore']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def charge(self) -> str:
        """If the skeleton moves at least 10 feet straight toward a target and then hits it with a gore attack on the same turn, the target takes an extra 9 (2d8) piercing damage. If the target is a creature, it"""
        return 'If the skeleton moves at least 10 feet straight toward a target and then hits it with a gore attack on the same turn, the target takes an extra 9 (2d8) piercing damage. If the target is a creature, it'

    def greataxe_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 17 (2d12 + 4) slashing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 17 (2d12 + 4) slashing damage.'

    def gore_attack(self) -> str:
        """Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) piercing damage."""
        return 'Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) piercing damage.'

