# bases1/clay-golem.py
"""
ClayGolem creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=clay-golem
"""
from creature_base import GlobalCreatureBaseClass


class ClayGolem(GlobalCreatureBaseClass):
    """
    Large construct creature - ClayGolem
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 133, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 9, 'CON': 18, 'INT': 3, 'WIS': 8, 'CHAR': 1, 'armor_class': 14, 'alignment': 'unaligned Armor Class  14 (natural armor) Hit Points  133 (14d10 + 56) Speed  20 ft. STR 20 (+5) DEX 9 (-1) CON 18 (+4) INT 3 (-4) WIS 8 (-1) CHA 1 (-5) Damage Immunities  acid', 'legendary': False, 'size': 'Large', 'type': 'construct', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['acid_absorption', 'multiattack', 'slam', 'haste_(recharge_5-6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def acid_absorption(self) -> str:
        """Whenever the golem is subjected to acid damage, it takes no damage and instead regains a number of hit points equal to the acid damage dealt.Berserk. Whenever the golem starts its turn with 60 hit poi"""
        return 'Whenever the golem is subjected to acid damage, it takes no damage and instead regains a number of hit points equal to the acid damage dealt.Berserk. Whenever the golem starts its turn with 60 hit poi'

    def multiattack_attack(self) -> str:
        """The golem makes two slam attacks."""
        return 'The golem makes two slam attacks.'

    def slam_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 16 (2d10 + 5) bludgeoning damage. If the target is a creature, it must succeed on a DC 15 Constitution saving throw or have its hit point maximum reduced by an amount equal to the damage taken. The target dies if this attack reduces its hit point maximum to 0. The reduction lasts until removed by the greater restoration spell or other magic."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 16 (2d10 + 5) bludgeoning damage. If the target is a creature, it must succeed on a DC 15 Constitution saving throw or have its hit point maximum reduced by an amount equal to the damage taken. The target dies if this attack reduces its hit point maximum to 0. The reduction lasts until removed by the greater restoration spell or other magic.'

    def haste_(recharge_5-6)_attack(self) -> str:
        """Until the end of its next turn, the golem magically gains a +2 bonus to its AC, has advantage on Dexterity saving throws, and can use its slam attack as a bonus action."""
        return 'Until the end of its next turn, the golem magically gains a +2 bonus to its AC, has advantage on Dexterity saving throws, and can use its slam attack as a bonus action.'

