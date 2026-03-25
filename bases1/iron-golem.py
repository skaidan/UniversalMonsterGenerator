# bases1/iron-golem.py
"""
IronGolem creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=iron-golem
"""
from creature_base import GlobalCreatureBaseClass


class IronGolem(GlobalCreatureBaseClass):
    """
    Large construct creature - IronGolem
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 210, 'min_level': 1, 'level': 1, 'STR': 24, 'DEX': 9, 'CON': 20, 'INT': 3, 'WIS': 11, 'CHAR': 1, 'armor_class': 20, 'alignment': 'unaligned Armor Class  20 (natural armor) Hit Points  210 (20d10 + 100) Speed  30 ft. STR 24 (+7) DEX 9 (-1) CON 20 (+5) INT 3 (-4) WIS 11 (+0) CHA 1 (-5) Damage Immunities  fire', 'legendary': False, 'size': 'Large', 'type': 'construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['fire_absorption', 'multiattack', 'slam', 'sword', 'poison_breath_(recharge_6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def fire_absorption(self) -> str:
        """Whenever the golem is subjected to fire damage, it takes no damage and instead regains a number of hit points equal to the fire damage dealt.Immutable Form. The golem is immune to any spell or effect """
        return 'Whenever the golem is subjected to fire damage, it takes no damage and instead regains a number of hit points equal to the fire damage dealt.Immutable Form. The golem is immune to any spell or effect '

    def multiattack_attack(self) -> str:
        """The golem makes two melee attacks."""
        return 'The golem makes two melee attacks.'

    def slam_attack(self) -> str:
        """Melee Weapon Attack: +13 to hit, reach 5 ft., one target. Hit: 20 (3d8 + 7) bludgeoning damage."""
        return 'Melee Weapon Attack: +13 to hit, reach 5 ft., one target. Hit: 20 (3d8 + 7) bludgeoning damage.'

    def sword_attack(self) -> str:
        """Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 23 (3d10 + 7) slashing damage."""
        return 'Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 23 (3d10 + 7) slashing damage.'

    def poison_breath_(recharge_6)_attack(self) -> str:
        """The golem exhales poisonous gas in a 15-foot cone. Each creature in that area must make a DC 19 Constitution saving throw, taking 45 (10d8) poison damage on a failed save, or half as much damage on a successful one."""
        return 'The golem exhales poisonous gas in a 15-foot cone. Each creature in that area must make a DC 19 Constitution saving throw, taking 45 (10d8) poison damage on a failed save, or half as much damage on a successful one.'

