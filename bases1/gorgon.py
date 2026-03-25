# bases1/gorgon.py
"""
Gorgon creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=gorgon
"""
from creature_base import GlobalCreatureBaseClass


class Gorgon(GlobalCreatureBaseClass):
    """
    Large monstrosity creature - Gorgon
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 114, 'min_level': 1, 'level': 1, 'STR': 20, 'DEX': 11, 'CON': 18, 'INT': 2, 'WIS': 12, 'CHAR': 7, 'armor_class': 19, 'alignment': 'unaligned Armor Class  19 (natural armor) Hit Points  114 (12d10 + 48) Speed  40 ft. STR 20 (+5) DEX 11 (+0) CON 18 (+4) INT 2 (-4) WIS 12 (+1) CHA 7 (-2) Skills  Perception +4 Condition Immunities  petrified Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Large', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': ['trampling_charge', 'gore', 'hooves', 'petrifying_breath_(recharge_5-6)']}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def trampling_charge(self) -> str:
        """If the gorgon moves at least 20 feet straight toward a creature and then hits it with a gore attack on the same turn, that target must succeed on a DC 16 Strength saving throw or be knocked prone. If """
        return 'If the gorgon moves at least 20 feet straight toward a creature and then hits it with a gore attack on the same turn, that target must succeed on a DC 16 Strength saving throw or be knocked prone. If '

    def gore_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 18 (2d12 + 5) piercing damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 18 (2d12 + 5) piercing damage.'

    def hooves_attack(self) -> str:
        """Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 16 (2d10 + 5) bludgeoning damage."""
        return 'Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 16 (2d10 + 5) bludgeoning damage.'

    def petrifying_breath_(recharge_5-6)_attack(self) -> str:
        """The gorgon exhales petrifying gas in a 30-foot cone. Each creature in that area must succeed on a DC 13 Constitution saving throw. On a failed save, a target begins to turn to stone and is restrained. The restrained target must repeat the saving throw at the end of its next turn. On a success, the effect ends on the target. On a failure, the target is petrified until freed by the greater restoration spell or other magic."""
        return 'The gorgon exhales petrifying gas in a 30-foot cone. Each creature in that area must succeed on a DC 13 Constitution saving throw. On a failed save, a target begins to turn to stone and is restrained. The restrained target must repeat the saving throw at the end of its next turn. On a success, the effect ends on the target. On a failure, the target is petrified until freed by the greater restoration spell or other magic.'

